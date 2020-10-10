# -*- coding: utf-8 -*-
# from odoo import http


# class GovBenePhils(http.Controller):
#     @http.route('/gov_bene_phils/gov_bene_phils/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gov_bene_phils/gov_bene_phils/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gov_bene_phils.listing', {
#             'root': '/gov_bene_phils/gov_bene_phils',
#             'objects': http.request.env['gov_bene_phils.gov_bene_phils'].search([]),
#         })

#     @http.route('/gov_bene_phils/gov_bene_phils/objects/<model("gov_bene_phils.gov_bene_phils"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gov_bene_phils.object', {
#             'object': obj
#         })
