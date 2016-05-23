from django.db import models
from mongoengine import *

# Create your models here.
class ShareEmployee(Document):
	employeeId = StringField(required=True)
	name = StringField(required=True)
	gender = StringField(required=True)

class Employee(Document):
	employeeId = StringField(required=True)
	shareEmployees = ListField(EmbeddedDocumentField('ShareEmployee'))
	name = StringField(required=True)
	gender = StringField(required=True)

class Menu(Document):
	juice = StringField(required=True)
	cost = StringField(required=True)