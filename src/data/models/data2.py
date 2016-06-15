es = []
ps = []
rs = []

def find_p(n,v, les=None):
    if not les:les=es
    a=filter(lambda x: x.name==n and x.value==v,ps)
    return map(lambda x: x.e,a)

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
    frm = filter(lambda x: x.name=='from',move.p)[0].getValue()
    to = filter(lambda x: x.name=='to',move.p)[0].getValue()
    frm_account=find_p('name',frm,a)
    to_account=find_p('name',to,a)

z = onevent('create',account_move)

print a1.p[0].name