import os, werkzeug, rdflib

from flask import Flask, render_template, flash, request, app

app = Flask(__name__)
app.secret_key = 'seekrit'

import urlpath
import parser
from redisConn import redisConn
from parser import Parser

@app.route('/')
def front():
    return "An attempt at writing a browser to explore RDF"

@app.route('/browser/<path:url>',methods=['GET', 'POST'])
def index(url):

    path = url
    dobj = {}
    if path is None:
        flash('You need to pass in a path')
    else: 
        r = redisConn()
        path_pts = urlpath.split_path(path)
        ppath =''
        
        if urlpath.urlpath(path_pts[0]) is True:
           # ppath = r.command('GET', urlpath.format_key(path_pts[1])) #variable needs a better name
            if not ppath:
                ppath = urlpath.get_url(path)

                #create the key
               # r.command('SET', urlpath.format_key(path_pts[1]), ppath) #variable needs a better name
               # r.command('SET TTL', urlpath.format_key(path_pts[1]), 120) #set for two minutes to live
                p = Parser()
                dobj = p.data_parse(path)
        else:
            print 'all false'
            flash('The url does not appear to be valid. Please check')  
    
    htmlstr = '<div id="parsedata">'
    for k, v in dobj.iteritems():
        htmlstr += "<p>%s</p>" % k
        for nk, nv in v.iteritems():
            htmlstr += '<p>----------</p><p>%s : %s</p>'% (nk, nv)
            #htmlstr += '<p>----------</p><p>'+str(nk)+' : '+str(nv)+'</p>'

    htmlstr += '</div>'
    return  htmlstr

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)