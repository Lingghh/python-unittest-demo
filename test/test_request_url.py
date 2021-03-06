# -*- coding: utf-8 -*-

import unittest
from mock import MagicMock
from app.request_url import RequestURL

class TestRequestURL(unittest.TestCase):
    
    def setUp(self):
        self.requestURL = RequestURL()
    
    
    def test_success_request(self):
        success_code = MagicMock(return_value='200')
        self.requestURL.send_request = success_code
        self.assertEqual(self.requestURL.get_visit_result("http://www.qq.com"), '200')
        
    def test_fail_request(self):
        fail_code = MagicMock(return_value='403')
        self.requestURL.send_request = fail_code
        self.assertEqual(self.requestURL.get_visit_result("http://www.qq.com"), '403')
