from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'

    x_progress = fields.Float(
        string='Porcentaje de progreso'
    )
