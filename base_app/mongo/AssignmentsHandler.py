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
    
    
    """
    CRUD - Update
    """

    def update_assignment(self, assignment: AssignedWeek):
        shift_id = assignment.get_shift_id()
        start_date = assignment.get_start_date()
        end_date = assignment.get_end_date()
        assignment_dict = assignment.get_dict_format()
        dailies = assignment_dict.get(Dailies)
        self.collection.find_one_and_update(
            {Shift_id: shift_id},
            {"$set":
                 {f"{Shift_id}": shift_id, f"{Start_date}": start_date, f"{End_date}": end_date,
                  f"{Dailies}": dailies}
             }, upsert=True
        )
