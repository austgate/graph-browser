import urllib2

def split_path(path):
    return path.split('://')
    
def urlpath(path):
    '''Test if valid url otherwise fail'''
    return bool(path == 'http' or path == 'https')
    

def format_key(path):
    return path.replace('/', '_')

def get_url (path):

    req = urllib2.Request(path)
    response = urllib2.urlopen(req)
    return response.read()