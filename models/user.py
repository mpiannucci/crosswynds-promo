from google.appengine.ext import db

class User(db.Model):
    ''' IP addresses that have accessed the promo '''
    email = db.StringProperty()
    referer = db.IntegerProperty()
    referal_id = db.IntegerProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)

def create_user(email, referer):
    ''' Add a new user to the database. If there is no referer, the code will be 0 '''
    new_user = User()
    new_user.email = email
    new_user.referer = referer

    # Get the newest user and increment the id counter
    query = db.Query(User)
    query.order('-created')
    if query.count(limit=1) > 0:
        new_user.referal_id = query[0].referal_id + 1
    else:
        new_user.referal_id = 1
    new_user.put()

    return new_user.referal_id

def delete_user(email):
    ''' Delete a user from the database '''
    user_query = db.Query(User)
    user_query.filter('email =', email)
    db.delete(user_query.get())

def get_user(email):
    ''' Get a user by email '''
    user_query = db.Query(User)
    user_query.filter('email =', email)
    return user_query.get()

def get_user_by_refid(refid):
    ''' Get a user by their referal id '''
    user_query = db.Query(User)
    user_query.filter('referal_id =', refid)
    return user_query.get()

def does_user_exist(email):
    ''' Get a boolean if the user exists in the database '''
    user = get_user(email)
    if user is None:
        return False
    return True

def get_referal_count(refid):
    ''' Get the number of referals for a given user '''
    found_user = get_user_by_refid(refid)

    if found_user is None:
        # Handle there not being any users found
        return 0

    # Find all the users with the user as a referer
    ref_query = db.Query(User)
    ref_query.filter('referer =', found_user.referal_id)
    return ref_query.count()