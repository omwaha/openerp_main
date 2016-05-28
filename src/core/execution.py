
from openerp import models, fields, api

class executer(models.Model):
    _name = 'stars.executer'
    
    name = fields.Char('Name')
    expression = fields.Text('Expression')
    
    functions = fields.Many2many('stars.function','Functions')
    
    stars = fields.One2many('stars.star', 'parent_executer', 'Stars')
    
    @api.one
    def execute(self):
        """sample expression:
        res = None
        for fun in self.functions:
            res = fun.execute()
        """
        pass

class function(models.Model):
    _name = 'stars.function'
    
    name = fields.Char('Name')
    expression = fields.Text('Expression')
    
    @api.one
    def execute(self,data_lst):
        pass