from modules import *
from timeline import app as timeline
from map import app as map
from table import app as table
from homepage import app as home
from counter import app as counter
from growth import app as growth

flask_app = Flask(__name__)

application = DispatcherMiddleware(flask_app, {
    '/home': home.server,
    '/counter': counter.server,
    '/timeline': timeline.server,
    '/map': map.server,
    '/table': table.server,
    '/growth': growth.server
})

# cherrypy.tree.graft(application, '/')
# cherrypy.engine.start()
# cherrypy.engine.block()
