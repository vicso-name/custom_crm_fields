{
    'name': 'Custom CRM Fields',
    'version': '1.0',
    'category': 'CRM',
    'summary': 'Adds custom fields to CRM leads for Umbele project',
    'author': 'Your Company',
    'website': 'https://umbeletown.com',
    'depends': ['crm'],
    'data': [
        'security/ir.model.access.csv',
	'security/crm_lead_status_rule.xml',
        'data/crm_brochure_data.xml',
	'data/crm_lead_status_data.xml',
        'views/crm_lead_view.xml',
	'views/crm_lead_kanban_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}

