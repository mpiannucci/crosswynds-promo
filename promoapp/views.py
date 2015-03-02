import web

class Index():
    '''Show the index page'''
    def GET(self):
        return "Hello World"