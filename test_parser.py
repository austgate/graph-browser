import unittest

import graphparser

class TestParser(unittest.TestCase):
    
    def setup_func(self):
        pass
        
    def teardown_func(self):
        self.graphdata = ''
        
    def test_readable_key_with_slash(self):
        gb = graphparser.GraphParser()
        testkey = gb.readable_key('http://xmlns.com/foaf/0.1/givenname')
        self.assertEqual('foaf::givenname', testkey)
        
    def test_readable_key_with_hash(self):
        gb = graphparser.GraphParser()
        testkey = gb.readable_key('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')
        self.assertEqual('rdf::type', testkey)