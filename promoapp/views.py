import web


class New:
    ''' The page shown to new users to prompt a sign up'''
    def GET(self):
        return "Show New Now"

class Refer:
    ''' 
    The page shown to users after they have signed up. This page tracks 
    referal counts and shows rewards
    '''
    def GET(self):
        return "Referal Shown"

class PrivacyPolicy:
    ''' Show the user the privacy policy '''
    def GET(self):
        return "Private"