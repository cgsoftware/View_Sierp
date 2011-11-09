# -*- encoding: utf-8 -*-

import pooler, tools

from osv import fields, osv

class mrp_production(osv.osv):
    

    def qty_available(self, cr, uid, ids,data, arg, context=None):
        var={}
        obj=self.pool.get('mrp.production')
        for riga in obj.browse(cr, uid, ids):
            qty = riga.product_id.qty_available
            var[riga.id] = {'qty_available': qty}
        return var    
   
# SE CALCOLA ANCHE LA GIACENZA VIRTUALE PERDE IL CALCOLO DELLA GIACENZA VIRTUALE
#    def virtual_available(self, cr, uid, ids, data, arg, context=None): 
#       var = {} 
#       obj=self.pool.get('mrp.production')
#       for riga in obj.browse(cr, uid, ids):
#              virtual = riga.product_id.virtual_available
#              var[riga.id]= {'virtual_available': virtual}
#       return var


    
    _inherit = 'mrp.production' 
    #Do not touch _name it must be same as _inherit
    #_name = 'mrp.production' cr
    _columns ={
               'qty_available' : fields.function(qty_available, method=True, string='Giacenza Reale', multi='sums'),
               #'virtual_available':fields.function(virtual_available, method=True, string='Giacenza Virtuale', multi='sums'),
               }
mrp_production()
