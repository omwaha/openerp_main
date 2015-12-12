# -*- coding: utf-8 -*-

import xmlrpclib

# url = 'http://localhost:9004'
# db = 'lead1'
# username = 'admin'
# password = 'admin'
# 
# common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url),allow_none=True)
# 
# models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url),allow_none=True)
# 
# def authinticate():
#     uid = common.authenticate(db, username, password, {})
# 
# def call(model,method,args=[],kw={}):
#     return models.execute_kw(db, 1, password, model, method,args, kw)
#     
# def search(model,args=[[]],kw={}):
#     return models.execute_kw(db, 1, password, model, 'search',args, kw)
# 
# def search_count(model,args=[[]],kw={}):
#     return models.execute_kw(db, 1, password, model, 'search_count',args, kw)
#     
# def read(model,args=[],kw={}):
#     return models.execute_kw(db, 1, password, model, 'read',args, kw)
# 
# def fields_get(model,args=[],kw={'attributes': ['string', 'type']}):
#     return models.execute_kw(db, 1, password, model, 'fields_get',args, kw)
# 
# def search_read(model,args=[[]],kw={}):
#     return models.execute_kw(db, 1, password, model, 'search_read',args, kw)
#     
# def write(model,args=[],kw={}):
#     return models.execute_kw(db, 1, password, model, 'write',args, kw)
# 
# def create(model,args=[],kw={}):
#     return models.execute_kw(db, 1, password, model, 'create',args, kw)
# 
# def unlink(model,args=[],kw={}):
#     return models.execute_kw(db, 1, password, model, 'unlink',args, kw)
 
class odoo_server:
    def __init__(self,db,user='admin',password='admin',host='localhost',port='8069'):
        self.url = 'http://'+host+':'+port
        self.db = db
        self.username = user
        self.password = password

class odoo_object:
    def __init__(self,name,server):
        self.server = server
        self.name = name
        self.uid = 0
        self.common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(self.server.url),allow_none=True)
        self.models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(self.server.url),allow_none=True)
        
    def authinticate(self):
        self.uid = self.common.authenticate(self.server.db, self.server.username, self.server.password, {})

    def call(self,method,args=[],kw={}):
        return self.models.execute_kw(self.server.db, self.server.uid, self.server.password, self.name, method,args, kw)
        
    def search(self,args=[[]],kw={}):
        return self.models.execute_kw(self.server.db, self.server.uid, self.server.password, self.name, 'search',args, kw)
    
    def search_count(self,args=[[]],kw={}):
        return self.models.execute_kw(self.server.db, self.server.uid, self.server.password, self.name, 'search_count',args, kw)
        
    def read(self,args=[],kw={}):
        return self.models.execute_kw(self.server.db, self.server.uid, self.server.password, self.name, 'read',args, kw)
    
    def fields_get(self,args=[],kw={'attributes': ['string', 'type']}):
        return self.models.execute_kw(self.server.db, self.server.uid, self.server.password, self.name, 'fields_get',args, kw)
    
    def search_read(self,args=[[]],kw={}):
        return self.models.execute_kw(self.server.db, self.server.uid, self.server.password, self.name, 'search_read',args, kw)
        
    def write(self,args=[],kw={}):
        return self.models.execute_kw(self.server.db, self.server.uid, self.server.password, self.name, 'write',args, kw)
    
    def create(self,args=[],kw={}):
        return self.models.execute_kw(self.server.db, self.server.uid, self.server.password, self.name, 'create',args, kw)
    
    def unlink(self,args=[],kw={}):
        return self.models.execute_kw(self.server.db, self.server.uid, self.server.password, self.name, 'unlink',args, kw)