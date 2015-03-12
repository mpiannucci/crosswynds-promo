import web
import models
import mailers
import config

from google.appengine.api import users

render = web.render

class Admin:
    ''' The handler for the admin page '''

    def GET(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            return render.admin()
        else:
            return render.admin()
            #raise web.redirect(users.create_login_url('/admin'))