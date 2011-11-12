# -*- encoding: utf-8 -*-

import pooler, tools

from osv import fields, osv
class stock_move(osv.osv):
    def carrier_id(self, cr, uid, ids,data, arg, context=None):
        var={}
        obj=self.pool.get('stock.move')
        for riga in obj.browse(cr, uid, ids):
            #import pdb;pdb.set_trace()
            car_id = riga.picking_id.carrier_id
            var[riga.id] = {'carrier_id' : car_id}
        return var
    _inherit = 'stock.move'
    _columns = {
                'carrier_id': fields.function(carrier_id, method=True, string='Trasportatore', multi='sums')
                }
stock_move()
    
            
            
            
