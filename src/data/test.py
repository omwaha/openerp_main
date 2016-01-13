from odoo_api import odoo_object,odoo_server

server = odoo_server('db')
records = odoo_object('data.record',server)
keys = odoo_object('data.key',server)

records.create({'name':'select all records',
                'type':'selection',
                'keys':[{'name':'select_all_records',
                         'values':[{'exp':'[]'},
                                   ]},
                        ]}
               )

K_selection_object = keys.create({'name':'selection_object', 'values':[{'exp':'$selection_object'},]})
R_selection_object_keys = records.create({'name':'selection object', 'keys':[K_selection_object], 'type':'data', 'vars':{'selection_object':'keys'}})

K_select_records_with_key = keys.create(
            {'name':'select_records_with_key',
             'values':[
                    {'exp':"['keys','=','$select_key']", },
                    ],
             'attributes':[R_selection_object_keys]
            },)

