from google.appengine.ext import db

class User(db.Model):
    '''IP addresses that have accessed the promo'''
    email = db.StringProperty()
    refcode = db.StringProperty()
    refid = db.IntegerProperty()
    created = db.DateTimeProperty()
    updated = db.DateTimeProperty(auto_now_add=True)