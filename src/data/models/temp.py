
from openerp import models, fields, api

class data_record(models.Model):
    _name = 'data.property'
    
    name = fields.Char('Name')
    value = fields.Text('Value')
    object = fields.Many2one('data.object', 'Object')


class data_object(models.Model):
    _name = 'data.object'
    
    name = fields.Char('Name')
    properties = fields.One2many('data.property','object', 'properties') 
 
    
class data_rules(models.Model):
    _name = 'data.rule'
    
    name = fields.Char('Name')
    event_cmds = fields.One2many('data.event.cmds', 'rule', 'Event Commands')


class data_event_cmds(models.Model):
    _name = 'data.event.cmds'
    
    event = fields.Many2one('data.event', 'Event')
    cmds = fields.One2many('data.cmd', 'event_cmds', 'Commands')
    rule = fields.Many2one('data.rule', 'Rule')


class data_event(models.Model):
    _name = 'data.event'
    
    type = fields.Selection([()], 'Type')
    query = fields.Many2one('data.query', 'Query')
    

class data_cmd(models.Model):
    _name = 'data.cmd'
    
    name = fields.Char('Name')
    query = fields.Many2one('data.query', 'Query')
    event_cmds = fields.Many2one('data.event.cmds', 'Event-Commands')

class data_query(models.Model):
    _name = 'data.query'
    
    name = fields.Char('Name')
    type = fields.Selection([('c','Create'),('r','Read'),('u','Update'),('d','Delete')], 'Type')
    
    
class data_query_statement(models.Model):
    _name = 'data.qeury.statement'
    
    name = fields.Char('Name')
    expr = fields.Text('Expression')
    type = fields.Selection([('c','Create'),('r','Read'),('u','Update'),('d','Delete')], 'Type')
    
    
    