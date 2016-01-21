
from openerp import models, fields, api

class star(models.Model):
    _name = 'stars.star'
    
    _inherits = {'stars.selector':'star_selector'}
    
    name = fields.Char('Name')
    
    selector_levels = fields.One2many('stars.selector.level','star','Selector Levels', ondelete='cascade')
     
    executer = fields.Many2one('stars.executer', 'Executer')
    
    data_stream = fields.One2many('stars.data', 'stream','Data')
    data_store = fields.Many2many('stars.data', string='Data Store')
    
    marks = fields.One2many('stars.mark','star', 'Marks')
    
    @api.one
    def consume(self,data_lst):
        self.select(data_lst)
        self.executer.execute()
    
    @api.one
    def select(self,data_lst):
        sdata_lst = data_lst
        for sl in self.selector_levels:
            sdata_lst = sl.select(sdata_lst)
            if not sdata_lst:
                break
        
        if sdata_lst:
            self.data_stream = self.data_stream+sdata_lst
        else:
            self.data_stream = []

      
class mark(models.Model):
    _name = 'stars.mark'
    
    name = fields.Char('Name')
    data = fields.Many2one('stars.data', 'Data')
    star = fields.Many2one('stars.star','Star')
    
class data(models.Model):
    _name = 'stars.data'
    
    key = fields.Char('key')
    
    value = fields.Char('value', compute='_compute_value')
    exp = fields.Text('Expression')
    
    sub_data = fields.One2many('stars.data', 'parent', 'Sub-Data')
    parent = fields.Many2one('stars.data','Parent')
    
    stream = fields.Many2one('stars.data.stream','Stream')
    
    @api.one
    @api.depends('exp')
    def _compute_value(self):
        pass