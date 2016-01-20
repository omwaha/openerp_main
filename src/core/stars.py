
from openerp import models, fields, api


class star(models.Model):
    _name = 'stars.star'
    
    _inherits = {'stars.selector':'star_selector'}
    
    name = fields.Char('Name')
    
    #selector_levels = fields.One2many('stars.selector.level','star','Selector Levels')
    
    star_selector = fields.Many2one('stars.star.selector','star Selector', required=True, ondelete='cascade')
    
    executer = fields.Many2one('stars.executer', 'Executer')
    functions = fields.Many2many('stars.function','Functions')
    
    data_stream = fields.One2many('stars.data', 'stream','Data')
    data_store = fields.Many2many('stars.data', string='Data Store')
    
    marks = fields.One2many()
    
    @api.one
    def on_new_data(self,data):
        #new_data = 
        self.star_selector.select(self,data)
    
    
    @api.one
    def write(self,vals):
        if vals.has_key('data_stream'):
            #if vals[data_stream] = [4,4,..]:
            self.on_new_data(vals['data_stream'])

class star_selector(models.Model):
    _name = 'stars.star.selector'
    
    star = fields.Many2one('stars.star', 'star')
    selector_levels = fields.One2many('stars.selector.level','star','Selector Levels')
    
    selected_data = fields.Many2many('stars.data', string='Selected Data')
    
    @api.one
    def select(self,star,data):
        self.selected_data = data
        for sl_lvl in self.selector_levels:
            sl_lvl.select(star,data)

class selection_level(models.Model):
    _name = 'stars.selector.level'
    
    selectors = fields.Many2many('stars.selector',string='Selectors')
    star = fields.Many2one('stars.star', 'star')
    seq = fields.Integer('Sequence')
    
    @api.one
    def select(self,star,data):
        for sel in self.selectors:
            sel.apply(data,star)
            
     
class selector(models.Model):
    _name = 'stars.selector'
    
    name = fields.Char('Name')
    type = fields.Selection([('selector','Selector'),('star','star')], 'Type')
    star = fields.Many2one('stars.star', 'Selector star')
    selector = fields.Many2one('stars.selector.selector', 'Selector')
    
    @api.one
    def apply(self,data,star):
        if self.type == 'selector':
            pass
        elif self.type == 'star':
            pass
          
class selector_selector(models.Model):
    _name = 'stars.selector.selector'
    
    selection_exp = fields.Text('Selection Expression')
    
    @api.one
    def apply(self,data,star,selector_lvl):
        #query the data
        star.marks += self.env['stars.mark'].create({'name':'', 'data': data})
        star.star_selector.selected_data += data
        pass
      
class mark(models.Model):
    _name = 'stars.mark'
    
    name = fields.Char('Name')
    data = fields.Many2one('stars.data', 'Data')
    
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