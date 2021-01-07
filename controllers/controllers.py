# -*- coding: utf-8 -*-
# from odoo import http


# class ReportesProject(http.Controller):
#     @http.route('/reportes_project/reportes_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reportes_project/reportes_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('reportes_project.listing', {
#             'root': '/reportes_project/reportes_project',
#             'objects': http.request.env['reportes_project.reportes_project'].search([]),
#         })

#     @http.route('/reportes_project/reportes_project/objects/<model("reportes_project.reportes_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reportes_project.object', {
#             'object': obj
#         })
