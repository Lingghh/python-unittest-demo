# -*- coding: utf-8 -*-
import requests

class Functions(object):
    
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2;
    
    def strange_add(self, num1, num2):
        return self.add(num1,num2) * 2
