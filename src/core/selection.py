
from openerp import models, fields, api

class selection_level(models.Model):
    _name = 'stars.selector.level'
    
    selectors = fields.Many2many('stars.selector',string='Selectors')
    star = fields.Many2one('stars.star', 'star')
    seq = fields.Integer('Sequence')
    
    
    @api.one
    def select(self,data_lst):
        sdata_set = set()
        for sel in self.selectors:
            for data in data_lst:
                sdata_lst = sel.select(data,self.star)
                if sdata_lst:
                    for sdata in sdata_lst:
                        sdata_set.add(sdata)
                
        return list(sdata_set)
            
     
class selector(models.Model):
    _name = 'stars.selector'
    
    name = fields.Char('Name')
    selection_exp = fields.Text('Selection Expression')
    
    @api.one
    def select(self,data,star):
        #query the data
        sdata = data
        star.marks += self.env['stars.mark'].create({'name':'mark1', 'data': sdata})
        #return [data]
        return sdata