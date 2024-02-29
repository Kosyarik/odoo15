from odoo import models, fields, http

class TrainingProgramme(models.Model):
    _name = 'training.programme'
    _description = 'Training Programme'

    week = fields.Integer(string='Week')
    module = fields.Char(string='Module')
    description = fields.Text(string='Description')
    sequence = fields.Integer(string='Sequence')
    event_id = fields.Many2one('event.event', string='Event')

    def update_sequence(self, sequence_values):
        try:
            if sequence_values:
                sequence_values = json.loads(sequence_values)
                training_programmes = self.env['training.programme'].browse(sequence_values)
                for index, training_programme in enumerate(training_programmes):
                    training_programme.sequence = index + 1
                self.env.cr.commit()
            return True
        except Exception as e:
            return False

    # all users have full access
    def _check_access_rights(self, operation):
        pass