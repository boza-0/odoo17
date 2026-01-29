from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    x_quality_status = fields.Selection(
        selection=[
            ('good', 'Bueno'),
            ('average', 'Regular'),
            ('bad', 'Malo'),
        ],
        string='Estado de calidad',
        default='good',
        required=True,
        tracking=True
    )
