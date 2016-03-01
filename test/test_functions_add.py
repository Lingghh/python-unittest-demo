# -*- coding: utf-8 -*-

import unittest
from app.functions import Functions
from mock import MagicMock, PropertyMock

class TestFunctionsAdd(unittest.TestCase):
    
    def setUp(self):
        self.functions = Functions()
    
    def test_add_1(self):
        self.assertEquals(self.functions.add(10,10),20)
    
    def test_add_2(self):
        self.assertEquals(self.functions.add(0,0), 0)
        
