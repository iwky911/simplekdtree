from plancomparator import *

class kdNode:
    
    def __init__(self, v, comp=None):
        self.value=v
        self.comparator=comp
        self.isLeaf= True
            
    def addElt(self, elt):
        if self.isLeaf:
            moy = elt.mean(self.value)
            self.comparator = PlanComparator(moy, elt)
            left = kdNode(self.value)
            right = kdNode(elt)
            self.value=moy
            self.setChildren(left, right)
        else:
            #~ print "inserting in node: ",self.getChildren(elt).value.values
            self.getChildren(elt).addElt(elt)
        
    def getNearest(self, elt):
        if self.isLeaf:
            return self.value if self.value == elt else None
        else:
            return self.getChildren(elt).getNearest(elt)
            
    def getChildren(self, elt):
        return self.children[1] if self.comparator.isAfter(elt) else self.children[0]
    
    def setChildren(self, left, right):
        self.children= (left, right)
        self.isLeaf = False
