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

class usuarios_login(models.Model):
	_name = 'usuarios.iniciar'
	name = fields.One2many('sesiones.usuarios', 'empleado', 'Usuarios', required=True)
	edad = fields.Integer()
	cargo = fields.Char("Cargo", required=True)
	direccion = fields.Char("Direccion", required=True)
	descripcion = fields.Text()
	
	""""class notas_curso(models.Model):
	    _name = 'notas.curso'
	    name = fields.Char(string="Nombre", required=True)
	    direccion = fields.Char('Direccion', size=100, required=True)
	    descripcion = fields.Text()	"""