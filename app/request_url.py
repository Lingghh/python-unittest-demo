# -*- coding: utf-8 -*-

import requests

class RequestURL(object):
    def send_request(self, url):
        r = request.get(url)
        return r.status_code
        
    def get_visit_result(self, url):
        return self.send_request(url)
        
