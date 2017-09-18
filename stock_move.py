# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api, _
#import time

class stock_move(models.Model):
	_inherit = 'stock.move'

	# @api.depends('product_id','product_uom_qty')
	# def calculate_uda(self):
	# 	value = 0
	# 	for rec in self:
	# 		if rec.product_id.presentation_pieces == 0:
	# 			return value
	# 		else:
	# 			value = rec.product_uom_qty / rec.product_id.presentation_pieces
	# 			rec.uda = value
	# 			return value
	@api.one
	@api.depends('product_id','product_uom_qty')
	def calculate_uda(self):
		if self.product_id.presentation_pieces == 0:
			self.uda = 0
		else:
			self.uda = self.product_uom_qty / self.product_id.presentation_pieces

	@api.one
	@api.onchange('product_id','product_uom_qty')
	def _get_product_oum_qty_uda(self):
		if self.product_id.presentation_pieces == 0:
			self.uda = 0
		else:
			self.uda = self.product_uom_qty / self.product_id.presentation_pieces


	uda = fields.Float('Unidad de almacenamiento', compute='calculate_uda', store=True)
	product_categ_id = fields.Many2one(string='Categoria del producto', store=True, related='product_id.categ_id')