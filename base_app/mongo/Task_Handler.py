from bson import ObjectId

from Collection_Handler import CollectionHandler
from .Models.Task import Task
from .constants import *


class TasksHandler(CollectionHandler):
    def __init__(self):
        CollectionHandler.__init__(self, "Tasks")

    """
    CRUD - Create
    """

    def add_new_task(self, task):
        data = dict()
        data[Task_id] = "Temp"
        data[Company_id] = task.get_company_id()
        data["TeamID"] = task.get_team_id()
        data["ParentalTaskID"] = "None"
        data["TaskInfo"] = task.get_task_info()
        data["StartDate"] = task.get_start_date()
        data["EndDate"] = task.get_end_date()
        data["Deadline"] = task.get_deadline()
        data["Priority"] = task.get_priority()
        data["Difficulty"] = task.get_difficulty()
        data["SubTasksID"] = task.get_sub_tasks()
        data["Status"] = task.get_status()
        data["AncestorTaskID"] = "None"
        task_id = str(self.collection.insert_one(data).inserted_id)
        data["TaskID"] = task_id
        doc = self.collection.find_one_and_update(
            {"_id": ObjectId(task_id)},
            {"$set":
                 {"TaskID": task_id}
             }, upsert=True
        )

    def add_sub_task(self, parent_task, task):
        data = dict()
        data["TaskID"] = "Temp"
        data["CompanyID"] = task.get_company_id()
        data["TeamID"] = task.get_team_id()
        data["ParentalTaskID"] = parent_task.get_task_id()
        data["TaskInfo"] = task.get_task_info()
        data["StartDate"] = task.get_start_date()
        data["EndDate"] = task.get_end_date()
        data["Deadline"] = task.get_deadline()
        data["Priority"] = task.get_priority()
        data["Difficulty"] = task.get_difficulty()
        data["SubTasksID"] = task.get_sub_tasks()
        data["Status"] = task.get_status()
        data["AncestorTaskID"] = parent_task.get_ancestor_task_id()
        task_id = str(self.collection.insert_one(data).inserted_id)
        doc = self.collection.find_one_and_update(
            {"_id": ObjectId(task_id)},
            {"$set":
                 {"TaskID": task_id}
             }, upsert=True
        )
        parent_id = parent_task.get_task_id()
        subtasks = parent_task.get_sub_tasks()
        subtasks.append(task_id)

        doc = self.collection.find_one_and_update(
            {"_id": ObjectId(parent_id)},
            {"$set":
                 {"SubTasksID": subtasks}
             }, upsert=True
        )

    """
    CRUD - Read
    """

    def __get_task_from_doc(self, doc):
        task_id = doc["TaskID"]
        parental_task_id = doc["ParentalTaskID"]
        team_id = doc["TeamID"]
        company_id = doc["CompanyID"]
        task_info = doc["TaskInfo"]
        start_date = doc["StartDate"]
        end_date = doc["EndDate"]
        deadline = doc["Deadline"]
        priority = doc["Priority"]
        difficulty = doc["Difficulty"]
        status = doc["Status"]
        sub_task_id = doc["SubTasksID"]
        ancestor_task_id = doc["AncestorTaskId"]
        task = Task(company_id=company_id, team_id=team_id, parental_task_id=parental_task_id, task_info=task_info,
                    startdate=start_date, deadline=deadline, enddate=end_date, priority=priority, difficulty=difficulty,
                    sub_tasks=sub_task_id, status=status, ancestor_task_id=ancestor_task_id, task_id=task_id)
        return task

    def get_active_ancestor_tasks_by_team(self, team_id):
        tasks = []
        query = {"TeamID":team_id, "Status": False, "AncestorTaskID": "None"}
        docs = self.collection.find(query, {})
        for doc in docs:
            tasks.append(self.__get_task_from_doc(doc))
        return tasks

    def get_tasks_by_ancestor_id(self, ancestor_id):
        tasks = []
        query = {"AncestorTaskID": ancestor_id}
        docs = self.collection.find(query, {})
        for doc in docs:
            tasks.append(self.__get_task_from_doc(doc))
        return tasks

    def get_tasks_by_team_id(self, team_id):
        tasks = []
        query = {"TeamID": team_id}
        docs = self.collection.find(query, {})
        for doc in docs:
            tasks.append(self.__get_task_from_doc(doc))
        return tasks

    def get_tasks_by_company_id(self, company_id):
        tasks = []
        query = {"CompanyID": company_id}
        docs = self.collection.find(query, {})
        for doc in docs:
            tasks.append(self.__get_task_from_doc(doc))
        return tasks


    """
    CRUD - Update
    """

    def update_task_status(self, task_id):
        self.collection.find_one_and_update(
            {"_id": ObjectId(task_id)},
            {"$set":
                 {"TaskID": task_id}
             }, upsert=True
        )

    """
    Crud - Delete
    """

# th = TasksHandler()
# th.get_active_ancestor_tasks_by_team(team_id="0")
