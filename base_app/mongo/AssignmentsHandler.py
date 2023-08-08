import pymongo
from bson import ObjectId

from base_app.mongo.Models.PostAssignment.AssignedWeek import AssignedEvent, AssignedDay, AssignedWeek
from base_app.mongo.Collection_Handler import CollectionHandler
from base_app.mongo.constants import *


class Assignment_Handler(CollectionHandler):
    def __init__(self):
        CollectionHandler.__init__(self, Assignment_Col)

    """
    CRUD - Create
    """

    def add_new_assignment(self, assignment: AssignedWeek):
        flag = self.update_assignment(assignment=assignment)
        if flag is True:
            return
        else:
            assignment_dict = assignment.get_dict_format()
            self.collection.insert_one(assignment_dict)


    """
    CRUD - Read
    """

    def get_assignment_by_shift_id(self, shift_id):
        assignment = None
        query = {f"{Shift_id}": shift_id}
        docs = self.collection.find(query, {})
        for doc in docs:
            assignment = AssignedWeek.dict_to_week_obj(doc)
        return assignment

    def get_recent_assignments_by_team_id(self, team_id, count=10):
        '''
        returns a Schedule object
        '''
        assignments = []
        pipeline = [
            {
                "$match": {
                    f"{Team_id}": team_id
                }
            },
            {
                "$sort": {
                    f"{Start_date}": pymongo.DESCENDING
                }
            },
            {
                "$limit": count
            }
        ]
        docs = self.collection.aggregate(pipeline=pipeline)
        for doc in docs:
            assignments.append(AssignedWeek.dict_to_week_obj(doc))
        return assignments

    def get_dated_assignments_by_team_id(self, team_id, date):
        '''
        returns a Schedule object
        '''
        assignment = None
        pipeline = [
            {
                "$match": {
                    f"{Team_id}": team_id,
                    "StartDate": {"$lte": date},
                    "EndDate": {"$gte": date}
                }
            },
            {
                "$sort": {
                    f"{Start_date}": pymongo.DESCENDING
                }
            },
        ]
        docs = self.collection.aggregate(pipeline=pipeline)
        for doc in docs:
            assignment = AssignedWeek.dict_to_week_obj(doc)
        return assignment

    def get_bounded_dated_assignments_by_team_id(self, team_id, start_date, end_date):
        '''
        returns a Schedule object
        '''
        assignments = []
        pipeline = [
            {
                "$match": {
                    f"{Team_id}": team_id,
                    "StartDate": {"$gte": start_date},
                    "EndDate": {"$lte": end_date}
                }
            },
            {
                "$sort": {
                    f"{Start_date}": pymongo.DESCENDING
                }
            },
        ]
        docs = self.collection.aggregate(pipeline=pipeline)
        for doc in docs:
            assignments.append(AssignedWeek.dict_to_week_obj(doc))
        return assignments

    """
    CRUD - Update
    """

    """
    Update assignment function, is used also in order to know if an assignment for the specific ShiftID exists,
    since if it doesn't exist, it will not do anything.
    Outputs:
    True: The assignment already exists and already updated, therefore there is no need to create new document.
    False: The assignment doesn't exist, therefore nothing will be updated, and we will need to create new document.
    """

    def update_assignment(self, assignment: AssignedWeek):
        shift_id = assignment.get_shift_id()
        start_date = assignment.get_start_date()
        end_date = assignment.get_end_date()
        assignment_dict = assignment.get_dict_format()
        team_id = assignment.get_team_id()
        company_id = assignment.get_company_id()
        dailies = assignment_dict.get(Dailies)
        query = {Shift_id: shift_id}
        to_update = {"$set":
                     {f"{Shift_id}": shift_id, f"{Start_date}": start_date,
                      f"{End_date}": end_date, f"{Team_id}": team_id,
                      f"{Company_id}": company_id, f"{Dailies}": dailies}
                     }
        result = self.collection.find_one_and_update(
            query, to_update, upsert=False)
        if result is not None:
            return True
        return False
