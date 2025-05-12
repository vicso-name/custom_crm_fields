from odoo import models, fields, api

# ===== Брошюры для выбора пользователем =====
class CrmBrochure(models.Model):
    _name = 'crm.brochure'
    _description = 'CRM Brochure'

    name = fields.Char(string="Brochure Name", required=True)


# ===== Расширение модели лида (crm.lead) =====
class CrmLead(models.Model):
    _inherit = 'crm.lead'

    telegram_username = fields.Char(string="Telegram Username")
    whatsapp_username = fields.Char(string="WhatsApp Username")

    status_id = fields.Many2one(
        'crm.lead.status',
        string="Status",
        index=True,
        tracking=True,
        group_expand='_group_expand_status_id'
    )

    lead_source = fields.Selection([
        ('website', 'Website'),
        ('roger', 'Roger'),
        ('nicole', 'Nicole'),
        ('sally', 'Sally'),
        ('unknown', 'Unknown'),
    ], string="Lead Source")

    keyword = fields.Char(string="Keyword", default="Now")

    brochures_received = fields.Many2many(
        'crm.brochure',
        string="Brochures Received",
        help="Select multiple brochures"
    )

    rental = fields.Selection([
        ('tenant', 'Tenant'),
        ('landlord', 'Landlord')
    ], string="Rental")

    @api.model
    def _group_expand_status_id(self, statuses, domain, order):
        """Показывать все статусы в канбане, даже если они пустые"""
        return self.env['crm.lead.status'].search([], order=order)
