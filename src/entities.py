"""
    @author: pascal de ladurantaye
    
"""

from google.appengine.ext import ndb


class Response(ndb.Model):
    sigle = ndb.StringProperty()
    no1 = ndb.IntegerProperty()
    no2 = ndb.IntegerProperty()
    no3 = ndb.IntegerProperty()
    no4 = ndb.IntegerProperty()
    no5 = ndb.IntegerProperty()
    no6 = ndb.IntegerProperty()
    no7 = ndb.IntegerProperty()
    no8 = ndb.IntegerProperty()
    no9 = ndb.IntegerProperty()
    no10 = ndb.IntegerProperty()
    no11 = ndb.IntegerProperty()
    no12 = ndb.IntegerProperty()
    no13 = ndb.IntegerProperty()
    no14 = ndb.IntegerProperty()
    no15 = ndb.IntegerProperty()
    no16 = ndb.IntegerProperty()
    no17 = ndb.IntegerProperty()
    no18 = ndb.IntegerProperty()
    no19 = ndb.IntegerProperty()
    no20 = ndb.IntegerProperty()
    no21 = ndb.IntegerProperty()
    no22 = ndb.IntegerProperty()
    no23 = ndb.IntegerProperty()
    no24 = ndb.IntegerProperty()
    no25 = ndb.IntegerProperty()
    no26 = ndb.IntegerProperty()
    no27 = ndb.IntegerProperty()
    no28 = ndb.IntegerProperty()

    no29 = ndb.TextProperty()
    no30 = ndb.TextProperty()


class Respondant(ndb.Model):
    creationDate = ndb.DateTimeProperty(auto_now_add=True)
    matricule = ndb.StringProperty(indexed=True)
    responses = ndb.StructuredProperty(Response, repeated=True)



