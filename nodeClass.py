class Node(object):
    def __init__(self,cor=[-1,-1]):
        self.cor = cor
        self.block = -1 # 1 blocked, 0 unblocked, -1 not defined
        self.rNode = self
        self.lNode = self
        self.uNode = self
        self.dNode = self
        self.tree = self
        self.search = 0
        self.gVal =0
    def __eq__(self,other):
        return (self.cor[0] == other.cor[0] and self.cor[1] == other.cor[1])
    def __gt__(self,other):
        return self.cor[0] > other.cor[0] or (self.cor[0] == other.cor[0] and self.cor[1]>other.cor[1])
    def __lt__(self,other):
        return self.cor[0] < other.cor[0] or (self.cor[0] == other.cor[0] and self.cor[1]<other.cor[1])
    def __ne__(self,other):
        return  self.cor[0] != other.cor[0] or  self.cor[1]!=other.cor[1]

def h_fun(start,end):
    x = start.cor[0]-end.cor[0]
    y = start.cor[1]-end.cor[1]
    return abs(x)+abs(y)



