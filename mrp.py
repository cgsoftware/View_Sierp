# -*- encoding: utf-8 -*-

import pooler, tools

from osv import fields, osv

class mrp_production(osv.osv):
    _inherit = 'mrp.production' 
    #Do not touch _name it must be same as _inherit
    #_name = 'mrp.production' cr
    _columns ={
               'qty_available':fields.one2many('product.product', 'product_tmpl_id', 'Giacenza Reale'),
                'virtual_available':fields.one2many('product.product', 'product_tmpl_id', 'Giacenza Virtuale'),

               }
mrp_production()