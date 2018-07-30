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

from openerp import models


class stock_picking(models.Model):
    _inherit = 'stock.picking'

    def calculate_sum_ltrs(self, move_ids):
        suma = 0.0
        move_ids = self.move_lines
        if not move_ids:
            return suma
        else:
            for line in move_ids:
                suma += line.product_uom_qty * line.product_id.udv
            return suma

    def calculate_sum_weight(self, move_ids):
        suma = 0.0
        move_ids = self.move_lines
        if not move_ids:
            return suma
        else:
            real_user = self.env.uid
            self.env.uid = 1  # FIXME dangerous permission raise, used to print with user `almacen`
            for line in move_ids:
                suma += line.product_uom_qty * line.product_id.weight
            self.env.uid = real_user
            return suma
