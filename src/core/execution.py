
from openerp import models, fields, api

class executer(models.Model):
    _name = 'stars.executer'
    
    name = fields.Char('Name')
    expression = fields.Text('Expression')
    
    functions = fields.Many2many('stars.function','Functions')
    
    

class function(models.Model):
    _name = 'stars.function'
    
    name = fields.Char('Name')
    expression = fields.Text('Expression')
    
    