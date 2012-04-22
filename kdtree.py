from kdtree import *
from vector import *

class kdTree:
    
    def __init__(self):
        self.root = None
    
    def add(self, e):
        if self.root == None:
            self.root = knNode(e)
        else:
            self.root.addElt(e)
    
    def search(self, e):
        if self.root==None:
            return None
        (val, cost) = self.root.getNearest(e)
        return val
