from flask import Flask
import mlab
from models.task import Task
from flask_restful import Api
from resources.task_resource import *
from mongoengine import Document, StringField
from flask_jwt import JWT,jwt_required
mlab.connect()
#Flask co chuc nang tao framework cho app
app = Flask(__name__)
api = Api(app)
app.config["SECRET_KEY"] = "MY SECRET KEY"

all_tasks = Task.objects()
for task in all_tasks:
    print(mlab.item2json(task))

class LoginCredential:
    def __init__(self,id):
        self.id = id


class User(Document):
    username = StringField();
    password = StringField();

# user = User(user="admin",password="admin")
# user.save()

def authenticate(username, password):
    for user in User.objects().filter(username = username):
       if user.password == password:
            return LoginCredential(str(user.id))

def identity(payload):
     payload['identity']

jwt = JWT(app,authenticate,identity)

@app.route('/')
@jwt_required()
def hello_world():
    return 'Hello World!'

api.add_resource(TaskListRest,"/tasks")
api.add_resource(TaskRes,"/tasks/<task_id>")

if __name__ == '__main__':
    app.run()
