
from openerp import models, fields, api


class cell(models.Model):
    _name = 'cells.cell'
    
    _inherits = {'cells.selector':'cell_selector'}
    
    name = fields.Char('Name')
    
    #selector_levels = fields.One2many('cells.selector.level','cell','Selector Levels')
    
    cell_selector = fields.Many2one('cells.cell.selector','Cell Selector', required=True, ondelete='cascade')
    
    executer = fields.Many2one('cells.executer', 'Executer')
    functions = fields.Many2many('cells.function','Functions')
    
    data_stream = fields.One2many('cells.data', 'stream','Data')
    data_store = fields.Many2many('cells.data', string='Data Store')
    
    marks = fields.One2many()
    
    @api.one
    def on_new_data(self,data):
        #new_data = 
        self.cell_selector.select(self,data)
    
    
    @api.one
    def write(self,vals):
        if vals.has_key('data_stream'):
            #if vals[data_stream] = [4,4,..]:
            self.on_new_data(vals[data_stream])

class cell_selector(models.Model):
    _name = 'cells.cell.selector'
    
    cell = fields.Many2one('cells.cell', 'Cell')
    selector_levels = fields.One2many('cells.selector.level','cell','Selector Levels')
    
    selected_data = fields.Many2many('cells.data', string='Selected Data')
    
    @api.one
    def select(self,cell,data):
        self.selected_data = data
        for sl_lvl in self.selector_levels:
            sl_lvl.select(cell,data)

class selection_level(models.Model):
    _name = 'cells.selector.level'
    
    selectors = fields.Many2many('cells.selector',string='Selectors')
    cell = fields.Many2one('cells.cell', 'Cell')
    seq = fields.Integer('Sequence')
    
    @api.one
    def select(self,cell,data):
        for sel in self.selectors:
            sel.apply(data,cell)
            
     
class selector(models.Model):
    _name = 'cells.selector'
    
    name = fields.Char('Name')
    type = fields.Selection([('selector','Selector'),('cell','Cell')], 'Type')
    cell = fields.Many2one('cells.cell', 'Selector Cell')
    selector = fields.Many2one('cells.selector.selector', 'Selector')
    
    @api.one
    def apply(self,data,cell):
        if self.type == 'selector':
            pass
        elif self.type == 'cell':
            pass
          
class selector_selector(models.Model):
    _name = 'cells.selector.selector'
    
    selection_exp = fields.Text('Selection Expression')
    
    @api.one
    def apply(self,data,cell,selector_lvl):
        #query the data
        cell.marks += self.env['cells.mark'].create({'name':'', 'data': data})
        cell.cell_selector.selected_data += data
        pass
      
class mark(models.Model):
    _name = 'cells.mark'
    
    name = fields.Char('Name')
    data = fields.Many2one('cells.data', 'Data')
    
class data(models.Model):
    _name = 'cells.data'
    
    key = fields.Char('key')
    
    value = fields.Char('value', compute='_compute_value')
    exp = fields.Text('Expression')
    
    sub_data = fields.One2many('cells.data', 'parent', 'Sub-Data')
    parent = fields.Many2one('cells.data','Parent')
    
    stream = fields.Many2one('cells.data.stream','Stream')
    
    @api.one
    @api.depends('exp')
    def _compute_value(self):
        pass