import os, werkzeug, rdflib

from flask import Flask, render_template, flash, request, app

app = Flask(__name__)
app.secret_key = 'seekrit'

import urlpath
from graphparser import GraphParser

@app.route('/')
def front():
    return "An attempt at writing a browser to explore RDF"

@app.route('/browser/<path:url>',methods=['GET', 'POST'])
def index(url):
    '''
       View function to show the data in a human readable fashion
       @param string path:
          The url given in the browser
       @return string:
           Graph marked up in HTML
    '''

    dobj = {}
    if url is None:
        flash('You need to pass in a url')
    else: 
        path_pts = urlpath.split_path(url)
        ppath =''
        
        if urlpath.urlpath(path_pts[0]) is True:
            if not ppath:
                #ppath = urlpath.get_url(url)
                p = GraphParser()
                dobj = p.data_parse(url)
        else:
            flash('The url does not appear to be valid. Please check')  
    
    htmlstr = '<div id="parsedata">'
    for k in dobj:
        htmlstr += "<p>%s</p>" % k
        #for nk, nv in v.iteritems():
        #    htmlstr += '<p>----------</p><p>%s : %s</p>'% (nk, nv)
            #htmlstr += '<p>----------</p><p>'+str(nk)+' : '+str(nv)+'</p>'

    htmlstr += '</div>'
    return  htmlstr

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)