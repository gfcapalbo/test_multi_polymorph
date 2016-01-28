# -*- coding: utf-8 -*-
##############################################################################
#
#    This module copyright (C) 2016 Therp BV (<http://therp.nl>).
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
from openerp import models, fields, api


class poly_son1(models.Model):
    _name = 'poly.son1'
    _inherits = {'poly.father': 'polyfather_id'
    _description = ''



    polyfather_id = fields.Many2one(
        comodel_name='poly.father',
        required=True)


    field_son1 = fields.Char()

    @api.multi
    def tryout(self):
        import pudb
        pudb.set_trace()
        pass

