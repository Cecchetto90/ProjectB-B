from google.appengine.ext import ndb                    #librerie di App Engine

  #Da appaEngine importiamo il package di librerie ndb dove al suo interno c'Ã¨ Model Ã¨ una classe che identifica una  tabella


class Stanza(ndb.Model):
    stanza_id = ndb.StringProperty(required=True)
    nome_stanza = ndb.StringProperty(required=True)
    numero = ndb.IntegerProperty()
    piano = ndb.StringProperty()
    tipologia = ndb.StringProperty
    prezzo = ndb.FloatProperty()
    immagine = ndb.BlobProperty()
    immagine_mimetype = ndb.StringProperty()
