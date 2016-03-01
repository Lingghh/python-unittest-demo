# -*- coding: utf-8 -*-

import unittest
from app.functions import Functions
from mock import MagicMock, PropertyMock

class TestFunctionsStrangeAdd(unittest.TestCase):
    
    def setUp(self):
        self.functions = Functions()
    
    def test_add_1(self):
        self.assertEquals(self.functions.strange_add(10,10),40)
    
    def test_add_2(self):
        self.assertEquals(self.functions.strange_add(0,0), 0)
    
    def test_add_with_mock_true(self):
        num1 = 5
        num2 = 5
        add_return_value = MagicMock(return_value=10)
        self.functions.add = add_return_value
        # should be 20
        self.assertEquals(self.functions.strange_add(num1, num2), 20)
    
    def test_add_with_mock_fail(self):
        num1 = 5
        num2 = 5
        add_return_value = MagicMock(return_value=0)
        self.functions.add = add_return_value
        self.assertEquals(self.functions.strange_add(num1, num2),0)
        
        
        
        
