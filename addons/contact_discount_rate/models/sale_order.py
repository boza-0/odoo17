from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    x_sale_category_ids = fields.Many2many(
        comodel_name='x_sale_category',
        string='Categorías personalizadas'
    )
