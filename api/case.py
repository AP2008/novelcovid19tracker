#from modules import *
#from timeline import app as timeline
#from map import app as map
#from table import app as table
#from homepage import app as home
#from counter import app as counter
#from growth import app as growth
#from about_covid import app as about_covid
#from about import app as about_me

from flask import Flask, Response
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
# cherrypy.tree.graft(application, '/')
# cherrypy.engine.start()
# cherrypy.engine.block()
