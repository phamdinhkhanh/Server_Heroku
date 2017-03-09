from flask_restful import Resource, reqparse
from models.task import Task
import mlab

class TaskListRest(Resource):
    def get(self):
        tasks = Task.objects()
        task_json = mlab.list2json(tasks)
        return task_json

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name = "name", type = str, location = "json")
        parser.add_argument(age = "age", type = int, location = "json")
        parser.add_argument(local_id = "local_id", type = str, location = "json")
        parser.add_argument(color = "color", type = str, location = "json")
        parser.add_argument(gender = "gender", type = str, location = "json")

        body = parser.parse_args()

        name = body["name"]
        local_id = body["local_id"]
        color = body["color"]
        gender = body["gender"]
        age = body["age"]

        task = Task(name = name, local_id = local_id, age=age, gender = gender, color = color,done = False)
        task.save()

        added_task = Task.objects().with_id(task.id)
        return mlab.item2json(added_task)

class TaskRes(Resource):
    def get(self,task_id):
        task = Task.objects.with_id(task_id)
        return mlab.item2json(task)

    def delete(self,task_id):
        task = Task.objects.with_id(task_id)
        task.delete()

    def put(self,task_id):
        task = Task.objects.with_id(task_id)
        parser = reqparse.RequestParser

        parser.add_argument(name="name", type=str, location="json")
        parser.add_argument(age="age", type=int, location="json")
        parser.add_argument(local_id="local_id", type=str, location="json")
        parser.add_argument(color="color", type=str, location="json")
        parser.add_argument(gender="gender", type=str, location="json")

        body = parser.parse_args()

        name = body["name"]
        local_id = body["local_id"]
        color = body["color"]
        gender = body["gender"]
        age = body["age"]

        task.update(name = name, local_id = local_id, age = age, gender = gender, color = color, done = False)
        taskupdate = Task.objects.with_id(task_id)

        return mlab.item2json(taskupdate)
