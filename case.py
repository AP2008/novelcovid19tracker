from modules import *
#from timeline import app as timeline
#from map import app as map
#from table import app as table
from homepage import app as home
#from counter import app as counter
#from growth import app as growth
#from about_covid import app as about_covid
#from about import app as about_me
#import arc

flask_app = Flask(__name__)

application = DispatcherMiddleware(home.server, {
    '/home': home.server,
   # '/counter': counter.server,
   # '/timeline': timeline.server,
    #'/map': map.server,
  #  '/datatable': table.server,
   # '/growth': growth.server,
    #'/infocenter': about_covid.server,
  #  '/about': about_me.server
  #  '/arc-sw.js': arc.app
})

# cherrypy.tree.graft(application, '/')
# cherrypy.engine.start()
# cherrypy.engine.block()
