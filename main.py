import web

# Map out the urls
urls = (
    '/', 'Index'
)

# Define the web templates
t_globals = {
    'datestr': web.datestr,
    'len': len
}
render = web.template.render('templates', base='base', globals=t_globals)

# Create the web app and the sessions
app = web.application(urls, globals())

# Start the Web page class definitions
class Index:
    ''' Show the home page '''
    def GET(self):
        return "Hello World"

def notfound():
    ''' Create the not found page '''
    return web.notfound('Sorry, the page you were looking for was not found.')
    # You can use template result like below, either is ok:
    # return web.notfound(render.notfound())
    # return web.notfound(str(render.notfound()))

def internalerror():
    ''' Create the internal error page '''
    return web.internalerror('The server says: No soup for you!')

# Create the not found app
app.notfound = notfound
app.internalerror = internalerror

main = app.cgirun()