es = []
ps = []
rs = []

def find_p(n,v, les=None):
    if not les:les=es
    a=filter(lambda x: x.name==n and x.value==v,ps)
    return map(lambda x: x.e,a)

def get_p1(name,e):
    return filter(lambda x: x.name==name,e.p)[0].getValue()
    
def find_class(cls,les=None):
    find_p('class',cls,les)

class E():
    def __init__(self,name=None,p_tuple_lst=[]):
        self.name = name
        self.p = []
        for p in p_tuple_lst:
            P(self, p[0],p[1])
        es.append(self)


class P():
    def __init__(self,e,name,value):
        self.e = e
        self.name = name
        self.value = value
        if e: e.p.append(self)
        ps.append(self)
    
    def getVlaue(self):
        return self.value
    
    def add_p(self,name,value):
        P(self, name,value)

class R():
    def __init__(self,name):
        pass
        
        
class onevent():
    def __init__(self,event=None,q=None,cmd=None):
        self.event=event
        self.q=q
        self.cmd=cmd
        
    
a1 = E('account1',[('class','account'),('acc_type','cash')])
a2 = E('account2',[('class','account'),('acc_type','cash')])
m1 = E('acc-move',[('class','account-move'),('from','account1'),('to','account2'),('amount',20)])

def account_move():
    find_class('account-move')
def create_account_move(move):
    a=find_class('account')
    frm = get_p1('from',move)
    to = get_p1('to',move)
    amount = get_p1('amount',move)
    frm_account=find_p('name',frm,a)
    to_account=find_p('name',to,a)
    
    #modify debt,credit of frm and to accounts
    frm_account.add_p('debt', amount)
    to_account.add_p('credit', amount)

z = onevent('create',account_move)

print a1.p[0].name