# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from werkzeug.exceptions import NotFound

from odoo.http import Controller, request, route, content_disposition


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
            # Отримайте дані про порядок з POST-запиту
            sequence_data = post.get('sequence_data')
            # Ваш код для оновлення порядку відповідно до sequence_data
            # Наприклад, викличте метод вашої моделі, який оновлює порядок
            # Поверніть успішну відповідь
            return Response('Sequence updated successfully', status=200)
        except Exception as e:
            # Обробка помилок
            return Response(str(e), status=500)