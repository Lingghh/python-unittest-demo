# -*- coding: utf-8 -*-

from app.services import RemovalService, UploadService

import mock
import unittest

class RemovalServiceTestCase(unittest.TestCase):
    
    @mock.patch('app.services.os.path')
    @mock.patch('app.services.os')
    def test_rm(self, mock_os, mock_path):
        # instantiate our service
        removal_service = RemovalService()
        
        # set up mock
        mock_path.isfile.return_value = False
        
        removal_service.rm("test_path")
        
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present")
        
        mock_path.isfile.return_value = True
        
        removal_service.rm("test_path")
        
        mock_os.remove.assert_called_with("test_path")
        
class UploadServiceTestCase(unittest.TestCase):
    
    @mock.patch.object(RemovalService, 'rm')
    def test_upload_complete(self, mock_rm):
        # build dependences
        removal_service = RemovalService()
        upload_service = UploadService(removal_service)
        
        # call upload_complete, which should call 'rm'
        upload_service.upload_complete("the uploaded file")
        
        # check that it called the rm method of any RemovalService
        mock_rm.assert_called_with("the uploaded file")
        
        #check that it called the rm method of _our_ removal_service
        removal_service.rm.assert_called_with('the uploaded file')
