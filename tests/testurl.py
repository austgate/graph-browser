import os
import flaskr
import unittest
import tempfile

import urlpath

class FlaskrTestCase(unittest.TestCase):
    #def setUp(self):
        
    #def tearDown(self):
        
    def testUrl1(self):
        path = 'http'
        assert(urlpath.urlpath(path), true)

    def testUrl2(self):
        path = 'https'
        assert(urlpath.urlpath(path), true) 
        
    def testUrl3(self):
        path = 'ftp'
        assert(urlpath.urlpath(path), false)           
        
if __name__ == '__main__':
    unittest.main()