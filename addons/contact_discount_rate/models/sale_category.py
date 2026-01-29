from odoo import models, fields

class SaleCategory(models.Model):
    _name = 'x_sale_category'
    _description = 'Categoría personalizada de venta'

    name = fields.Char(string='Nombre', required=True)
    color = fields.Integer(string='Color')
