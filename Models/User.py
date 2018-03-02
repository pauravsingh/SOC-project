from google.appengine.ext import ndb


class User(ndb.Model):
    id = ndb.IntegerProperty()
    name = ndb.StringProperty()
    favorites = ndb.IntegerProperty(repeated=True)
