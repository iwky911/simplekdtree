

class PlanComparator:
    """
    create a comparator to determine on wich part of the plan you are.
    """
    
    def __init__(self, start, end):
        self.ref = start
        self.dir = end.minus(start)
        
    def isAfter(self, elt):
        return elt.minus(self.ref).crossprod(self.dir)>=0

    def distToPlan(self, elt):
        return abs(elt.minus(self.ref).crossprod(self.dir)/float(self.dir.squaredlength()))
