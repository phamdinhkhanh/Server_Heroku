from mongoengine import *

class Task(Document):
      local_id = StringField();
      name = StringField();
      age = IntField();
      gender = StringField();
      color = StringField();
      done = BooleanField();