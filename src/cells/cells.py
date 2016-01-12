
from openerp import models, fields, api


class component(models.Model):
    _name = 'cells.component'
    
    name = fields.Char('Name')
    selectors = fields.One2many('cells.selector.level','component','Selector Levels')
    executer = fields.Many2one('cells.executer', 'Executer')
    functions = fields.Many2many('cells.function','Functions')
    
    marks = fields.One2many()

class selector(models.Model):
    _name = 'cells.selector'
    
    name = fields.Char('Name')
    type = fields.Selection([('selector','Selector'),('cell','Cell')], 'Type')
    cell = fields.Many2one('cells.cell', 'Selector Cell')
    selector = fields.Many2one('cells.selector.selector', 'Selector')
    
class selector_selector(models.Model):
    _name = 'cells.selector.selector'
    
    selection_exp = fields.Text('Selection Expression')
    
    @api.one
    def apply(self,data):
        pass
    
class selection_level(models.Model):
    _name = 'cells.selector.level'
    
    selectors = fields.Many2many('cells.selector','cell','Selectors')
    component = fields.Many2one('cells.component', 'Component')
    seq = fields.Integer('Sequence')
    
class mark(models.Model):
    _name = 'cells.mark'
    
    name = fields.Char('Name')
    data = fields.Many2one('cells.data', 'Data')
    
class cell(models.Model):
    _name = 'cells.cell'
    
    name = fields.Char('Name')
    data_stream = fields.One2many('cells.data', 'stream','Data')
    data_store = fields.Many2many('cells.data', string='Data Store')
    components = fields.Many2many('cells.component', string='Components')
    
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