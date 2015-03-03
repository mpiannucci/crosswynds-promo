import web

render = web.render

class New:
    ''' The page shown to new users to prompt a sign up'''
    email_form = web.form.Form(
        web.form.Textbox('email', web.form.notnull,
            size=23,
            description='',
            placeholder='Enter your email',
            class_='form-horizontal email-form'),
        web.form.Button('Sign Up', class_='btn btn-primary email-form')
    )

    def GET(self):
        form = self.email_form()
        return render.new(form)

    def POST(self):
        form = self.email_form()
        return render.new(form)

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
