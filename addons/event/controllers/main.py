# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from werkzeug.exceptions import NotFound

from odoo.http import Controller, request, route, content_disposition
from odoo import http


class EventController(Controller):

    @route(['/event/<model("event.event"):event>/ics'], type='http', auth="public")
    def event_ics_file(self, event, **kwargs):
        lang = request.context.get('lang', request.env.user.lang)
        if request.env.user._is_public():
            lang = request.httprequest.cookies.get('frontend_lang')
        event = event.with_context(lang=lang)
        files = event._get_ics_file()
        if not event.id in files:
            return NotFound()
        content = files[event.id]
        return request.make_response(content, [
            ('Content-Type', 'application/octet-stream'),
            ('Content-Length', len(content)),
            ('Content-Disposition', content_disposition('%s.ics' % event.name))
        ])
   
    @route(['/event/update_sequence'], type='http', auth="user", website=True, methods=['POST'])
    def update_sequence(self, **post):
        try:
            sequence_data = post.get('sequence_data')
            return Response('Sequence updated successfully', status=200)
        except Exception as e:
            return Response(str(e), status=500)

    @http.route('/event/add_training_programme', type='http', auth='user', website=True)
    def add_training_programme(self, **post):
        # Code to handle adding a new training programme
        return http.request.render('my_module.add_training_programme_template')

    @http.route('/event/view_training_programme/<int:training_programme_id>', type='http', auth='user', website=True)
    def view_training_programme(self, training_programme_id, **post):
        # Code to handle viewing a training programme
        return http.request.render('my_module.view_training_programme_template', {'training_programme_id': training_programme_id})
