from google.appengine.ext import db

class IPAddress(db.Model):
    ''' IP addresses that have accessed the promo '''
    address = db.StringProperty()
    count = db.IntegerProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)

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

def get_ip_address(address):
    ''' Get an ip address from the datastore '''
    address_query = db.Query(IPAddress)
    address_query.filter('address =', address)
    return address_query.get()

def get_ip_count(address):
    ''' Check the hits from the given ip address '''
    address_query = db.Query(IPAddress)
    address_query.filter('address =', address)
    if address_query.count(limit=1) > 0:
        address = address_query.get()
        return address.count
    else:
        return 0

def increment_ip_count(address):
    ''' Increment the ip count of the login address '''
    address_query = db.Query(IPAddress)
    address_query.filter('address =', address)
    if address_query.count(limit=1) > 0:
        address = address_query.get()
        address.count += 1
        address.put()