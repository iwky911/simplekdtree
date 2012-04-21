
import pytest
from vector import *
from plancomparator import *
from kdtree import *

class TestVector:
    def setup(self):
        self.v1= Vector([1,2,3,6,5])
        self.v2 = Vector([0,0,-2,-1,1])
    
    def test_should_be_able_to_process_crossprods(self):
        assert self.v1.crossprod(self.v2) == -7
    
    def test_minus_should_return_the_right_result(self):
        assert self.v1.minus(self.v2) == Vector([1,2,5,7,4])

    def test_plus_add_each_component_of_the_vectors(self):
        assert self.v1.plus(self.v2) == Vector([1,2,1,5,6])
    
    def test_equal_vectors_should_be_equal(self):
        assert Vector([0,2]) == Vector([0.0,2.0])

class TestPlanComparator:
    def setup(self):
        self.v1= Vector([0,1,0,6])
        self.v2 = Vector([0,1,1,0])
        self.comp = PlanComparator(self.v1, self.v2)
    
    def test_should_detect_sides_of_random_vectors(self):
        assert self.comp.isAfter(Vector([0,2,3,6]))
        assert not self.comp.isAfter(Vector([0,0,-1,6]))
        
    def test_disttoplan_should_return_the_distance_to_the_plan(self):
        comp = PlanComparator(Vector([1,1]), Vector([0,1]))
        assert comp.distToPlan(Vector([2,0])) == 1

class TestKdTree:
    def setup(self):
        center = Vector([0,0])
        startdir = Vector([1,1])
        comp = None
        self.tree = kdNode(center)
        self.v1=Vector([0,8])
        self.v2 = Vector([4,-2])
        self.v3 = Vector([8,0])

    def test_append_vectors_should_be_lookable(self):
        self.tree.addElt(self.v1)
        self.tree.addElt(self.v2)
        #~ self.tree.addElt(self.v3)
        assert self.v1 == self.tree.getNearest(self.v1)[0]
    
    def test_getNearest_should_return_the_closest_element_in_the_tree(self):
        self.tree.addElt(self.v1)
        self.tree.addElt(self.v2)
        self.tree.addElt(self.v3)
        assert self.v1 == self.tree.getNearest(Vector([1,8]))[0]
        
    
    
    
    
