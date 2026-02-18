from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    custom_note = fields.Char(string="Custom Note")
