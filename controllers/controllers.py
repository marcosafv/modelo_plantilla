# -*- coding: utf-8 -*-
from openerp import http

# class CreatMod1(http.Controller):
#     @http.route('/creat_mod1/creat_mod1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/creat_mod1/creat_mod1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('creat_mod1.listing', {
#             'root': '/creat_mod1/creat_mod1',
#             'objects': http.request.env['creat_mod1.creat_mod1'].search([]),
#         })

#     @http.route('/creat_mod1/creat_mod1/objects/<model("creat_mod1.creat_mod1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('creat_mod1.object', {
#             'object': obj
#         })