from mongoengine import *


class Checkpoint(EmbeddedDocument):
    miles = FloatField(required=True)
    km = FloatField(required=True)
    location = StringField()
    open_time_field = StringField(required=True)
    close_time_field = StringField(required=True)

class Brevet(Document):
    brevet_dist_km = FloatField(required=True)
    begin_date = StringField(required=True)
    items = EmbeddedDocumentListField(Checkpoint, required=True)