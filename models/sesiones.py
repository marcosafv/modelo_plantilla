# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class creat_mod1(models.Model):
#     _name = 'creat_mod1.creat_mod1'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class sesiones_usuarios(models.Model):
	_name = 'sesiones.usuarios'
	empleado = fields.Many2one('usuarios.iniciar','Usuarios', required=True, help='Ingrese un usuario')
	hora_entrada = fields.Integer()
	hora_salida = fields.Integer()
	fecha = fields.Date()