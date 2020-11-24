import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_neg_more_than(self) :
        source = inspect.getsource(negationGreaterThan)
        self.assertTrue( source.find("if")!=-1, "there should be an if statement in negationGreaterThan" )
        for n in range(10) : 
            self.assertTrue( numberGreaterThan(data,n)==len(data) - negationGreaterThan(data,n), "negationGreaterThan is not working correctly" )
        
    def test_neg_less_than(self) :
        source = inspect.getsource(negationLessThan)
        self.assertTrue( source.find("if")!=-1, "there should be an if statement in negationLessThan" )
        for n in range(10) : 
            self.assertTrue( numberLessThan(data,n)==len(data) - negationLessThan(data,n), "negationLessThan is not working correctly" )
            
    def test_neg_more_than(self) :
        source = inspect.getsource(negationEqualTo)
        self.assertTrue( source.find("if")!=-1, "there should be an if statement in negationEqualTo" )
        for n in range(10) : 
            self.assertTrue( numberEqualTo(data,n)==len(data) - negationEqualTo(data,n), "negationEqualTo is not working correctly" )
