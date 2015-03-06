import web
import models
import mailers
import config

render = web.render

email_validator = web.form.regexp(r".*@.*.", "Must be a valid email address")
email_form = web.form.Form(
    web.form.Textbox('email', email_validator,
        size=23,
        description='',
        placeholder='Enter your email',
        class_='form-horizontal email-form'),
    web.form.Button('Enter', type='submit', description='Enter', class_='btn btn-primary email-form')
)

class Index:
    ''' The base handler for the web page '''
    def GET(self, referer=0):
        form = email_form()
        return render.new(form)

    def POST(self, referer=0):
        if referer is None:
            # Handle an empty url
            referer = 0
        form = email_form()
        if form.validates():
            email = form.d.email
            ip = web.ctx.ip

            if models.does_user_exist(email):
                # If the user already exists, treat this as a log in and show 
                # them their referal page
                user = models.get_user(email)
                raise web.seeother('/refer/' + str(user.referal_id))
            else:
                # Check the ip count and block if theres already more than 2 requests
                ip_count = models.get_ip_count(ip)
                if ip_count > 2:
                    models.increment_ip_count(ip)
                    return render.ip_block()
                else:
                    if ip_count > 0:
                        models.increment_ip_count(ip)
                    else:
                        models.create_ip_address(ip)
                    # Create a new user
                    refid = models.create_user(email, int(referer))
                    ref_url = "/" + str(refid)
                    
                    # TODO: Send confirmation email
                    
                    raise web.seeother('/refer/' + str(refid))
        else:
            return render.new(form)

class Refer:
    ''' 
    The page shown to users after they have signed up. This page tracks 
    referal counts and shows rewards
    '''
    def GET(self, refid=0):
        if refid is None:
            # Handle an empty url
            refid = 0

        # Get the score and pass it to the referal page
        score = models.get_referal_count(int(refid))
        ref_url = config.base_url + refid
        return render.refer(score, ref_url)

class PrivacyPolicy:
    ''' Show the user the privacy policy '''
    def GET(self):
        return render.privacy()
