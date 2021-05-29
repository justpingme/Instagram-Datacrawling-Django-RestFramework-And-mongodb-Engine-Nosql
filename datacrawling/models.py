from mongoengine.fields import EmbeddedDocumentField, StringField, ListField, EmailField
from mongoengine.document import Document, EmbeddedDocument
from mongoengine.queryset.base import CASCADE

# Create your models here.

class Post(EmbeddedDocument):
    message = StringField(max_length=500, required=True, default='')
    tags = ListField(StringField(max_length=50))


class Brand(Document):
    name = StringField(max_length=100)
    bio = StringField(max_length=500, default='')
    post = ListField(EmbeddedDocumentField(Post))

    meta = {'allow_inheritance': True}

class Comment(EmbeddedDocument):
    username = StringField(max_length=50, required=True)
    comment = StringField(max_length= 500, default='')

class InfluencerPost(EmbeddedDocument):
    likes = StringField(max_length=50)
    message = StringField(max_length= 500, required=True, default='')
    tags = ListField(StringField(max_length=50),required=False, default=list)
    comment = ListField(EmbeddedDocumentField(Comment))

    meta = {'allow_inheritance': True}

class Influencer(Document):
    ig_link = StringField(max_length=200, required=True, default='')
    bio = StringField(max_length= 500,default='')
    email_id = EmailField(required=False,default='')
    followers = StringField(max_length=50)
    post = ListField(EmbeddedDocumentField(InfluencerPost))

    meta = {'allow_inheritance': True}

    
