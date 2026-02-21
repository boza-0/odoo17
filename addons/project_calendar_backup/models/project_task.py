from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'

    planning_date = fields.Datetime(
        string='Fecha de planificación'
    )
