from google.appengine.ext import ndb

class Opportunity(ndb.Model):
    id = ndb.KeyProperty()
    name = ndb.StringProperty()
    url = ndb.StringProperty()
    description = ndb.TextProperty()
    deadline = ndb.StringProperty()
    date = ndb.StringProperty()
    tags = ndb.StringProperty()

