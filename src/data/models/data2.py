
from openerp import models, fields, api

class data_record(models.Model):
    _name = 'data.record'
    
    name = fields.Char('Name',size=500,required=True)
    path = fields.Text('Path', compute='_compute_path')
    
    keys = fields.Many2many('data.key',string='Keys')
    
    sub_records = fields.One2many('data.record','parent','Sub Records')
    parent = fields.Many2one('data.record','Parent Record')
    
    store = fields.Many2one('data.store','Store')
    layers = fields.Many2many('data.layer', string='Layers')
    
    type = fields.Selection([('data','Data'),('function','Function'),('selection','Selection')])
    
    @api.depends('parent','name')
    @api.one
    def _compute_path(self):
        path = ''
        if self.name:
            path = '/'+self.name[:5]
        parent = self.parent
        while parent:
            path = '/'+parent.name[:5]+path
            parent = parent.parent
        self.path = path
        
class data_key(models.Model):
    _name = 'data.key'
    
    key = fields.Char('Key',size=500)
    values = fields.Many2many('data.value',string='Values')
    
    attributes = fields.Many2many('data.record',string='Attributes')
    
class value(models.Model):
    _name = 'data.value'
    
    exp = fields.Char('Expression',size=1000)
    content = fields.Char('Content',size=1000,compute='_compute_content') 
    
    @api.one
    def _compute_content(self):
        pass
    
class data_store(models.Model):
    _name = 'data.store'
    
    records = fields.One2many('data.record','store','Records')
    attributes = fields.Many2many('data.record',string='Attributes')
    
class data_layer(models.Model):
    _name = 'data.layer'
    
    name = fields.Char('Layer', size=300)
    