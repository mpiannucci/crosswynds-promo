import web


# Map out the urls
urls = (
    '/', 'New'
)

# Define the web templates
t_globals = {
    'datestr': web.datestr,
    'len': len
}
render = web.template.render('templates', base='base', globals=t_globals)

# Create the web app and the sessions
app = web.application(urls, globals())


class New:
    ''' The page shown to new users to prompt a sign up'''
    def GET(self):
        return render.new()

class Refer:
    ''' 
    The page shown to users after they have signed up. This page tracks 
    referal counts and shows rewards
    '''
    def GET(self):
        return render.refer()

class PrivacyPolicy:
    ''' Show the user the privacy policy '''
    def GET(self):
        return render.private()

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