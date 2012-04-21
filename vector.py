

class Vector:
    
    def __init__(self, val):
        self.values=val
        self.n = len(val)
    
    def minus(self, v):
        return Vector([self.values[i]-v.values[i] for i in range(len(self.values))])

    def crossprod(self, v):
        return reduce(lambda x,y: x+y, [self.values[i]*v.values[i] for i in range(len(self.values))])

    def __eq__(self, v):
        if(v==None):
            return False
        print self.values,"vs",v.values
        return reduce(lambda x,y: x and y, [float(self.values[i])==float(v.values[i]) for i in range(len(self.values))])
        
    def plus(self, v):
        return Vector([self.values[i]+v.values[i] for i in range(len(self.values))])

    def mean(self, v):
        return Vector([(self.values[i]+v.values[i])*0.5 for i in range(self.n)])
