from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    soluzion_id = fields.Char(
        string='Soluzion_ID'
    )
