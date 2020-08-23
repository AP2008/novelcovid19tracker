from modules import *
from timeline import app as timeline
from map import app as map
from table import app as table
from homepage import app as home
from counter import app as counter
from growth import app as growth
from about_covid import app as about_covid
from about import app as about_me

flask_app = Flask(__name__)

app = DispatcherMiddleware(home.server, {
    '/home': home.server,
    '/counter': counter.server,
    '/timeline': timeline.server,
    '/map': map.server,
    '/table': table.server,
    '/growth': growth.server,
    '/infocentre': about_covid.server,
    '/aboutme': about_me.server
})

# cherrypy.tree.graft(application, '/')
# cherrypy.engine.start()
# cherrypy.engine.block()
