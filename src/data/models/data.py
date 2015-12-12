
from openerp import models, fields, api

class data_record(models.Model):
    _name = 'data.record'
    
    #data fields
    name = fields.Char('Name',size=500,required=True)
    path = fields.Text('Path', compute='_compute_path')
    
    
    key = fields.Char('Key',size=500)
    value = fields.Many2many('data.value',string='Value')
    str_value = fields.Char('Value',size=500,compute='_compute_str_value')
    
    functions = fields.Many2many('data.function', string='Functions')
    
    tunnel = fields.Many2one('data.record','Tunnel')
    
    sub_records = fields.One2many('data.record','parent','Sub Records')
    parent = fields.Many2one('data.record','Parent Record')
    
    store = fields.Many2one('data.store','Store')
    
    layers = fields.Many2many('data.layer', string='Layers', help='Layers are used to control the visibility of data records, comma separated list of names')
    
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
        
    @api.one
    def copy(self, default=None):
        res = super(data_record,self).copy(default)
        new_sub_recs = self.env['data.record']
        for rec in self.sub_records:
            new_sub_recs += rec.copy(default)
        res.sub_records = new_sub_recs
        return res
    
    @api.one
    def evaluate(self):
        if self.no_evaluate:
            return
        
        if self.evaluate_childs_first :
            self._eval_childs()
            self._eval_self()
        else:
            self._eval_self()
            self._eval_childs()
        
        if self.remove:
            self.parent = self.trash_record
        
    @api.one
    def _eval_childs(self):
        for record in self.sub_records:
            record.evaluate()
             
    @api.one
    def _eval_self(self):
        value = self.value
        ''
        #produce a new record
        if self.produce and self.parent and self.parent.parent:
            self.parent = self.parent.parent
    
    
    @api.one
    def _compute_str_value(self):
        string=''
        for v in self.value:
            string += v.content+', '
        self.str_value = string
    
    @api.multi
    def edit_btn(self):
        return {'name': self.name or 'Record '+set(self.id),
                'view_type': 'form',
                'view_mode': 'form',
                'view_id': False,
                'res_model': 'data.record',
                'res_id':self.id,
#                 'domain':[('id','=',self.id ) ],
                'type': 'ir.actions.act_window',
#                 'target': 'new',
                }
        
class data_store(models.Model):
    _name = 'data.store'
    
    records = fields.One2many('data.record','store','Records')
    meta_data = fields.Many2one('data.record','Meta Data')

# class evaluation_enviroment(models.Model):
#     _name = 'data.evaluation.enviroment'
#     
#     records = fields.Many2many('data.record',string='Records')
#     meta_data = fields.Many2one('data.record','Meta Data')
#     
#     available_layers = fields.Many2many('data.layer', string='Available Layers', compute='_compute_available_layers')
#     visible_layers = fields.Many2many('data.layer', string='Visible Layers', help='comma separated list of visible layers names')
#     
#     @api.depends('records')
#     @api.one
#     def _compute_available_layers(self):
#         self.available_layers = self.records.mapped('layer')
#         
# class record_evaluation(models.Model):
#     _name = 'data.record.evaluation'
#     
#     record = fields.Many2one('data.record','Record')
#     result = record.evaluate()
#     variables_binding
    
class value(models.Model):
    _name = 'data.value'
    
    content = fields.Char('Content',size=1000)  

class data_layer(models.Model):
    _name = 'data.layer'
    
    name = fields.Char('Layer', size=300)
        
class data_function(models.Model):
    _name = 'data.function'
    
    name = fields.Char('Name',size=500)
    code = fields.Text('Code')
    
class data_selection(models.Model):
    _name = 'data.selection'
    
    name = fields.Char('Name',size=500)