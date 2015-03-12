# Map out the urls to their handlers
# The handlers/view controllers are defined in the 'views' module
urls = (
    '/(\d+)?', 'Index',
    '/refer/(\d+)?', 'Refer',
    '/privacy', 'PrivacyPolicy',
    '/admin', 'Admin'
)
