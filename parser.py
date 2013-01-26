'''
   Functions to deal with the data
'''
from rdflib.Graph import Graph

class Parser:

    def __init__(self):
        self.g = Graph()
        self.keys = {
             "http://xmlns.com/foaf/0.1/": 'foaf',
             'http://purl.org/dc/elements/1.1/': 'dc', 
             'http://purl.org/dc/terms/': 'dcterms',
             'http://www.w3.org/1999/02/22-rdf-syntax-ns#': 'rdf', 
             'http://www.w3.org/2004/02/skos/core#': 'skos'
             }

    def data_parse (self, triples):
        '''
        Function to parse the incoming triples and return a set to the browser
        '''
        self.g.parse(triples, format="xml")
        #rdf = self.g.parse(triples)
        rdf = {}
        for subject,predicate,obj_ in self.g:
            assert (subject,predicate,obj_) in self.g, "Iterator / Container Protocols are Broken!!"
            #@todo change this to list with dict inside
            rdf = {subject:{predicate: obj_}}
            #rdf.append(subject)
    
        return rdf

    def readable_key(self, pred):
        ''' 
           Function to swap the url into a key 
        '''
        read=''
        for k, v in self.keys.iteritems():
            if k in str(pred):
                print k
                read = v
            else:
                read = 'The key could not be found. Please update the list'
        
        return read