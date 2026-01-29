from odoo import models, fields

class HrContract(models.Model):
    _inherit = 'hr.contract'

    x_review_date = fields.Date(
        string='Fecha de revisión del contrato'
    )
