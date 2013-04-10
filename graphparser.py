'''
   Functions to deal with the data
'''
from rdflib.graph import Graph


class GraphParser:

    def __init__(self):
        # Set up the graph
        self.g = Graph()
        # Create a dictionary of urls and keys
        self.keys = {
             "http://xmlns.com/foaf/0.1/": 'foaf',
             'http://purl.org/dc/elements/1.1/': 'dc', 
             'http://purl.org/dc/terms/': 'dcterms',
             'http://www.w3.org/1999/02/22-rdf-syntax-ns#': 'rdf', 
             'http://www.w3.org/2004/02/skos/core#': 'skos',
             "http://www.w3.org/2000/01/rdf-schema#": 'rdfs'
             }

    def data_parse (self, triples):
        '''
           Function to parse the incoming triples and return a set to the browser
           @param string triples:
              The incoming string of triples from the url
        '''
        print 'triples' + triples
        self.g.parse('graph.xml', format="xml")

        rdf = []
        for subject,predicate,obj_ in self.g:
            #assert (subject,predicate,obj_) in self.g, "Iterator / Container Protocols are Broken!!"
            #@todo change this to list with dict inside
            
            rdf.append(self.readable_key(str(predicate)) + ':' + str(obj_))
            #rdf.append(subject)
            #print rdf
        return rdf

    def readable_key(self, pred):
        ''' 
           Function to swap the url into a key 
           http://xmlns.com/foaf/0.1/family_name should become 
           FOAF:family_name
           @param string pred:
              predicate
              
           @return string
              Human readable version of the 
        '''
        #first return the 
        npred = []
        if '#' in pred:
            npred = pred.split('#')
            last = '#'.join(npred[0:-1]) + '#'
        else:
            npred = pred.split('/')
            last = '/'.join(npred[0:-1]) + '/'

        if str(last) in self.keys:
            return self.keys[last] + '::' + npred[-1]
        else:
            return 'The key could not be found. Please update the list'

    


 
gb = GraphParser()

#print gb.readable_key(data)

for k in gb.data_parse(''):
    print k