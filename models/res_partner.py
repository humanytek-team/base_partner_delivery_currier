# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    delivery_currier = fields.Boolean(string='Delivery Currier')
