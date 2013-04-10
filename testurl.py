import os
import unittest
import tempfile

import urlpath

class FlaskrTestCase(unittest.TestCase):
    #def setUp(self):
        
    #def tearDown(self):
        
    def testUrl1(self):
        path = 'http'
        assert(urlpath.urlpath(path), True)

    def testUrl2(self):
        path = 'https'
        assert(urlpath.urlpath(path), True) 
        
    def testUrl3(self):
        path = 'ftp'
        assert(urlpath.urlpath(path), False)           
        
if __name__ == '__main__':
    unittest.main()