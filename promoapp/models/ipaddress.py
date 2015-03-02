from google.appengine.ext import db

class IPAddress(db.Model):
    '''IP addresses that have accessed the promo'''
    address = db.StringProperty()
    count = db.IntegerProperty()
    created = db.DateTimeProperty()
    updated = db.DateTimeProperty(auto_now_add=True)