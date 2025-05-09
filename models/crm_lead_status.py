from odoo import models, fields

class CrmLeadStatus(models.Model):
    _name = 'crm.lead.status'
    _description = 'Custom Lead Status for Kanban'

    name = fields.Char(string="Status", required=True)
    sequence = fields.Integer(string="Sequence", default=10)
    folded = fields.Boolean(string="Folded in Kanban", default=False)
