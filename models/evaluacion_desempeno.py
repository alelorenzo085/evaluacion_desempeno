from odoo import models, fields, api

class EvaluacionDesempeno(models.Model):
    _name = 'evaluacion.desempeno'
    _description = 'Evaluación de Desempeño'
    title = fields.Char(string='Título', required=True)
    description = fields.Text(string='Descripción')
    assigned_to = fields.Many2one('res.users', string='Usuario Asignado')
    deadline = fields.Date(string='Fecha de evaluación')
    state = fields.Selection([
        ('pending', 'Pendiente'),
        ('in_progress', 'En Progreso'),
        ('done', 'Finalizado'),
    ], string='Estado', default='pending')
    priority = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Media'),
        ('2', 'Alta'),
    ], string='Prioridad', default='1')

    @api.onchange('state')
    def _onchange_state(self):
        if self.state == 'done':
            self.priority = '0'  # Baja prioridad si está hecho