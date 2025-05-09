# -*- coding: utf-8 -*-
# from odoo import http


# class CustomCrmFields(http.Controller):
#     @http.route('/custom_crm_fields/custom_crm_fields', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_crm_fields/custom_crm_fields/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_crm_fields.listing', {
#             'root': '/custom_crm_fields/custom_crm_fields',
#             'objects': http.request.env['custom_crm_fields.custom_crm_fields'].search([]),
#         })

#     @http.route('/custom_crm_fields/custom_crm_fields/objects/<model("custom_crm_fields.custom_crm_fields"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_crm_fields.object', {
#             'object': obj
#         })

