import web
from config import urls

# Define the web templates
t_globals = {
    'datestr': web.datestr,
    'len': len
}
web.render = render = web.template.render('templates', base='base', globals=t_globals)

# Load the view controllers into the namespace now that the templates are loaded
from views import *

# Create the web app and the sessions
app = web.application(urls, globals())

# Define some callbacks for page not founds
def notfound():
    ''' Create the not found page '''
    return web.notfound('Sorry, the page you were looking for was not found.')
    # You can use template result like below, either is ok:
    # return web.notfound(render.notfound())
    # return web.no
    # tfound(str(render.notfound()))

def internalerror():
    ''' Create the internal error page '''
    return web.internalerror('The server says: No soup for you!')

# Create the not found app
app.notfound = notfound
app.internalerror = internalerror

main = app.cgirun()
