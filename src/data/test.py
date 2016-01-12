from odoo_api import odoo_object,odoo_server

server = odoo_server('db')
records = odoo_object('data.record',server)


records.create({'name':'select all records',
                'type':'selection',
                'keys':[{'name':'select_all_records',
                         'values':[{'exp':'[]'},
                                   ]},
                        ]}
               )