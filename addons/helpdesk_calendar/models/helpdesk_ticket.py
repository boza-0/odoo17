from odoo import models, fields

class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    planning_date = fields.Datetime(
        string="Fecha de planificación"
    )
