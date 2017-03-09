from flask import Flask
import mlab
from models.task import Task
from flask_restful import Api
from resources.task_resource import *

mlab.connect()
app = Flask(__name__)
api = Api(app)

# task = Task(name = "Khanh Pham", gender = "Male",age = 24,local_id="ajdhd-ạhfhh-dsah",color = "#2FE6G9",done = False)
# task.save()

# for i in range(10):
#     task = Task(name = "Khanh Pham Dinh"+str(i), local_id = "adbca-adafr-123"+str(i),color = "#2DF4H"+str(i))
#     task.save()


all_tasks = Task.objects()
for task in all_tasks:
    print(mlab.item2json(task))



# my_task = Task.objects(name = "Khanh Pham").first()
# print(mlab.item2json(my_task))


# my_task.update(set__done = True)


# for khanh in Task.objects():
#     khanh.delete()


@app.route('/')
def hello_world():
    return 'Hello World!'

api.add_resource(TaskListRest,"/tasks")
api.add_resource(TaskRes,"/tasks/<task_id>")

if __name__ == '__main__':
    app.run()
