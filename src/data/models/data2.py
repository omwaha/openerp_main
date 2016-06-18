es = []
ps = []
rs = []
vs = []

def findby_p(n,v, les=None):
    if not les:les=es
    a=filter(lambda x: x.name==n and x.value==v and x.e in les, ps)
    return map(lambda x: x.e,a)

def findby_name(n, les=None):
    if not les:les=es
    a=filter(lambda x: x.name==n and x in les, es)
    return a

def findby_class(cls,les=None):
    return findby_p('class',cls,les)
    
def get_p1(name,e):
    a=filter(lambda x: x.name==name,e.p)
    if a:return a[0].getValue()
    else: return None
def get_p1_or0(name,e):
    a=get_p1(name,e)
    if a==None: return 0
    else: return a
    

class E():
    def __init__(self,name=None,p_tuple_lst=[]):
        self.name = name
        self.p = []
        for p in p_tuple_lst:
            P(self, p[0],p[1])
        es.append(self)
        
        for v in filter(lambda x: x.event=='create',vs) : v.run(self)
    
    def add_p(self,name,value):
        P(self, name,value)
    def create_or_update_p(self,name,value):
        a=filter(lambda x: x.name==name,self.p)
        if a:a[0].setValue(value)
        else:self.add_p(name,value)
        
    def __str__(self):
        return str((self.name, map(lambda x: str(x),self.p) ))


class P():
    def __init__(self,e,name,value):
        self.e = e
        self.name = name
        self.value = value
        if e: e.p.append(self)
        ps.append(self)
    
    def getValue(self):
        return self.value
    def setValue(self,v):
        self.value = v
      
    def __str__(self):
        return str( (self.name,self.value) )

class R():
    def __init__(self,name,onevent_lst=[]):
        self.name=name
        for onev in onevent_lst:
            vs.append( onevent(self,onev[0],onev[1],onev[2]) )
        
        
class onevent():
    def __init__(self,r=None,event=None,q=None,cmd=None):
        self.event=event
        self.q=q
        self.cmd=cmd
        self.r=r
    
    def run(self,e):
        if self.q(e):
            self.cmd(e)
        
def account_move(e):
    return bool(findby_class('account-move',[e]))
def create_account_move(move):
    accounts=findby_class('account')
    frm = get_p1('from',move)
    to = get_p1('to',move)
    amount = get_p1('amount',move)
    frm_account=findby_name(frm,accounts)[0]
    to_account=findby_name(to,accounts)[0]
    
    #modify debt,credit of frm and to accounts
    frm_account.create_or_update_p('debt', get_p1_or0('debt',frm_account)+amount)
    to_account.create_or_update_p('credit', get_p1_or0('credit',to_account)+amount)
    
    print frm_account
    print to_account

z = R('account_move',[('create',account_move,create_account_move)] )


a1 = E('account1',[('class','account'),('acc_type','cash')])
a2 = E('account2',[('class','account'),('acc_type','cash')])

print a1
print a2

m1 = E('account-move',[('class','account-move'),('from','account1'),('to','account2'),('amount',20)])
m2 = E('account-move',[('class','account-move'),('from','account2'),('to','account1'),('amount',10)])



