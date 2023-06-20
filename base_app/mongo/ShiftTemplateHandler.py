import pymongo
from bson import ObjectId

from base_app.mongo.Models.ShiftTemplate import Shift_Template
from base_app.mongo.Collection_Handler import CollectionHandler
from base_app.mongo.constants import *

class Shift_Template_Handler(CollectionHandler):
    def __init__(self):
        CollectionHandler.__init__(self, Shift_Template_Col)

    def add_new_shift_template(self, shift_template: Shift_Template):
        template_dict = shift_template.serialize()
        template_id = str(self.collection.insert_one(template_dict).inserted_id)
        doc = self.collection.find_one_and_update(
            {"_id": ObjectId(template_id)},
            {"$set":
                 {f"{Template_id}": template_id}
             }, upsert=True
        )

    """
    Get all of the templates
    """

    def get_all_by_team_id(self, team_id):
        template_list = []
        query = {"TeamID": team_id}
        docs = self.collection.find(query, {})
        for doc in docs:
            template = Shift_Template.deserialize(doc)
            template_list.append(template)
        return template_list
    
    """
    Get a batch of templates
    """

    def get_batch_by_team_id(self, team_id: int, skip_count: int, count: int):
        templates = []
        pipeline = [
            {
                "$match": {
                    f"{Team_id}": team_id
                }
            },
            {
                "$skip": skip_count
            },
            {
                "$limit": count # TODO: define pagination (static 10 is OK for now)
            }
        ]
        docs = self.collection.aggregate(pipeline=pipeline)
        for doc in docs:
            templates.append(Shift_Template.deserialize(doc))
        return templates
    
    def update_template(self, shift_template: Shift_Template):
        template_id = shift_template.get_template_id()
        team_id = shift_template.get_team_id()
        start = shift_template.get_start_hour()
        end = shift_template.get_end_hour()
        needed_roles = shift_template.get_needed_roles()
        self.collection.find_one_and_update(
            {Template_id: template_id},
            {"$set":
                 {f"{Template_id}": template_id, f"{Team_id}": team_id, f"{Start_hour}": start, f"{End_hour}": end,
                  f"{NeededRoles}": needed_roles}
             }, upsert=True
        )

    def delete_template(self, template_id):
        filter = {Template_id: template_id}
        self.collection.delete_one(filter=filter)