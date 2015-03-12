import web
import models

from google.appengine.api import users

render = web.render

class Admin:
    ''' The handler for the admin page '''

    def GET(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            count = models.get_user_count()
            return render.admin(count, user)
        else:
            raise web.redirect(users.create_login_url('/admin'))

    def POST(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            all_users = models.get_all_users()
            email_list = []
            for user in all_users:
                email_list.append(user.email)
                email_list.append("\n")
            email_joined_list = "".join(email_list)
            web.header('Content-Type', 'text/plain')
            return email_joined_list
