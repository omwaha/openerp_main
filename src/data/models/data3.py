
Es = []
Ps = []

class E():
    def __init__(self,name=None,ds=[]):
        self.name = name
        self.ps = []
        for d in ds:
            self.ps.append( P(self,d) )
        Es.append(self)
        
    def add_p(self,d):
        self.ps.append( P(self,d) )

class P():
    def __init__(self,e=None,d=(None,None)):
        self.name = d[0]
        self.value = d[1]
        self.e = e
        Ps.append(self)
    
    def set_name(self,x):
        self.name = x
    def get_name(self):
        return self.name

a = E('account1',[('class','account')])

def aaa():
    
    a=filter(lambda x:x.name=='account1',Es)
    print a[0].name
    
aaa()