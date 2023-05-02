import pymongo
from bson import ObjectId

from .Models.Schedule import Shift,Schedule
from .Collection_Handler import CollectionHandler


class Shifts_Handler(CollectionHandler):
    def __init__(self):
        CollectionHandler.__init__(self, "Shifts")

    """
    Utilities
    """

    def get_schedule_from_doc(self, doc):
        shift_id = doc["ShiftID"]
        team_id = doc["TeamID"]
        company_id = doc["CompanyID"]
        start_date = doc["StartDate"]
        end_date = doc["EndDate"]
        sc = Schedule(company_id=company_id, team_id=team_id, startdate=start_date, enddate=end_date, shift_id=shift_id)
        for data in doc["DailyShifts"]:
            date = data["Date"]
            start_hour = data["StartHour"]
            end_hour = data["EndHour"]
            possible_shifts = data["PossibleShifts"]
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
                 {"ShiftID": shift_id}
             }, upsert=True
        )

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
                    "TeamID": team_id
                }
            },
            {
                "$sort": {
                    "StartDate": pymongo.DESCENDING
                }
            },
            {
                "$limit": 10
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
        query = {"ShiftID": shift_id}
        docs = self.collection.find(query, {})
        for doc in docs:
            sc = self.get_schedule_from_doc(doc)
        return sc
    
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
                 {"ShiftID": shift_id, "CompanyID": company_id, "TeamID": team_id, "StartDate": start, "EndDate": end,
                  "DailyShifts": shifts_register}
             }, upsert=True
        )

    """
    Crud - Delete
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
