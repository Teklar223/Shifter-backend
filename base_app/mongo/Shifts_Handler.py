import pymongo
from bson import ObjectId

from base_app.mongo.Models.Schedule import Shift,Schedule
from base_app.mongo.Collection_Handler import CollectionHandler
from base_app.mongo.constants import *


class Shifts_Handler(CollectionHandler):
    def __init__(self):
        CollectionHandler.__init__(self, Shifts_Col)

    """
    Utilities
    """

    def get_schedule_from_doc(self, doc):
        shift_id = doc[Shift_id]
        team_id =  int(doc[Team_id])
        company_id = int(doc[Company_id])
        start_date = int(doc[Start_date])
        end_date = int(doc[End_date])
        sc = Schedule(company_id=company_id, team_id=team_id, startdate=start_date, enddate=end_date, shift_id=shift_id)
        for data in doc[Daily_shifts]:
            date = int(data[Date])
            start_hour = int(data[Start_hour])
            end_hour = int(data[End_hour])
            possible_shifts = data[Possible_shifts]
            daily = Shift(date=date, starthour=start_hour, endhour=end_hour, possible_shifts=possible_shifts)
            sc.add_daily_shift(daily)
        return sc

    """
    Crud - Create
    """

    def add_new_shift(self, schedule: Schedule):
        s_dict = schedule.get_dict_format()
        shift_id = str(self.collection.insert_one(s_dict).inserted_id)
        doc = self.collection.find_one_and_update(
            {"_id": ObjectId(shift_id)},
            {"$set":
                 {f"{Shift_id}": shift_id}
             }, upsert=True
        )
        schedule.shift_id = shift_id
        return schedule

    """
    Crud - Read
    """
    # TODO - check if these functions should be moved to assignment handler
    def get_recent_shifts_by_team_id(self, team_id):
        '''
        returns a Schedule object
        '''
        schedules = []
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
                "$limit": 10 # TODO: define pagination (static 10 is OK for now)
            }
        ]
        docs = self.collection.aggregate(pipeline=pipeline)
        for doc in docs:
            schedules.append(self.get_schedule_from_doc(doc))
        return schedules

    def get_schedule_by_shift_id(self, shift_id):
        '''
        returns a Schedule object
        '''
        sc = None
        query = {f"{Shift_id}": shift_id}
        docs = self.collection.find(query, {})
        for doc in docs:
            sc = self.get_schedule_from_doc(doc)
        return sc
    
    def get_dated_shift_by_team_id(self, team_id, date):
        '''
        returns a Schedule object
        '''
        schedule = None
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
            schedule = self.get_schedule_from_doc(doc)
        return schedule
    
    def get_bounded_dated_shifts_by_team_id(self, team_id, start_date, end_date):
        '''
        returns a Schedule object
        '''
        schedules = []
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
            schedules.append(self.get_schedule_from_doc(doc))
        return schedules
    

    """
    Crud - Update
    """

    def update_shift(self, schedule: Schedule):
        shift_id = schedule.get_shift_id()
        company_id = schedule.get_company_id()
        team_id = schedule.get_team_id()
        start = schedule.get_start_date()
        end = schedule.get_end_date()
        shifts = schedule.get_daily_shifts()
        shifts_register = []
        for shift in shifts:
            shifts_register.append(shift.get_dict_format())
        s_dict = schedule.get_dict_format()
        self.collection.find_one_and_update(
            {"_id": ObjectId(shift_id)},
            {"$set":
                 {f"{Shift_id}": shift_id, f"{Company_id}": company_id, f"{Team_id}": team_id, f"{Start_date}": start, f"{End_date}": end,
                  f"{Daily_shifts}": shifts_register}
             }, upsert=True
        )

    def check_if_exist(self, schedule: Schedule):
        t_id = schedule.get_team_id()
        start = schedule.get_start_date()
        end = schedule.get_end_date()
        outputs = self.get_bounded_dated_shifts_by_team_id(team_id=t_id, start_date=start, end_date=end)
        if len(outputs) > 0:
            return outputs[0]
        else:
            return None

    

    """
    Crud - Delete # TODO
    """

# s = Shift(1, 1, 1, [{"ShiftName": "Evening", "StartHour": 1900, "EndHour": 2330, "NeededRoles":
#     [
#         {
#             "RoleID": 1500,
#             "NeededWorkers": 54
#         }
#     ],
#
#                      }
#                     ]
#           )
# sc = Schedule(9, 7, 9, 67, '643db236077a1bb573e4339a')
# sc.add_daily_shift(s)
# sh = Shifts_Handler()
# sh.update_shift(sc)
# sh.add_new_shift(sc)
# print(sh.get_recent_shifts_by_team_id(7)[0].get_dict_format())

