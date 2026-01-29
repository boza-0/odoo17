from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_discount_rate = fields.Float(
        string='Porcentaje de descuento especial'
    )
