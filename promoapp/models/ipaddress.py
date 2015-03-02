from google.appengine.ext import db

class IPAddress(db.Model):
    ''' IP addresses that have accessed the promo '''
    address = db.StringProperty()
    count = db.IntegerProperty()
    created = db.DateTimeProperty(auto_now_add=True)

def create_ip_address(address):
    ''' Add a new IP address entry '''
    ip = IPAddress()
    ip.address = address
    ip.count = 1
    ip.put()

def delete_ip_address(address):
    ''' Remove an IP address from the datastore '''
    address_query = db.Query(IPAddress)
    address_query.filter('address =', address)
    db.delete(address_query.get())

def get_ip_count(address):
    ''' Check the hits from the given ip address '''
    address_query = db.Query(IPAddress)
    address_query.filter('address =', address)
    if address_query.count() > 0:
        return address_query.get().count
    else:
        return 0