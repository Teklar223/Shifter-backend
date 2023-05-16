from bson import ObjectId
from .Models.WeeklyPref import DailyPref, WeeklyPref
from .Models.Schedule import Schedule
from .Models.Shift import Shift
from .Collection_Handler import CollectionHandler


class WeeklyPrefHandler(CollectionHandler):
    def __init__(self):
        CollectionHandler.__init__(self, "WeeklyPreferences")

    def derive_preferences_from_schedule(self, employee_id, schedule: Schedule, default_pref = False):
        # TOOD: add
        team_id = schedule.get_team_id()
        shift_id = schedule.get_shift_id()
        company_id = schedule.get_company_id()
        dailies = []
        wp = WeeklyPref(employee_id=employee_id, team_id=team_id, shift_id=shift_id, company_id=company_id,
                        dailies=dailies)
        for shift in schedule.get_daily_shifts():
            date = shift.get_date()
            data = shift.get_available_shifts()
            shift_types = []
            for available_shift in data:
                start_hour = available_shift["StartHour"]
                end_hour = available_shift["EndHour"]
                shift_name = available_shift["ShiftName"]
                answer = default_pref
                shift_types.append(
                    {"StartHour": start_hour, "EndHour": end_hour, "ShiftName": shift_name, "Answer": answer})
                constraints = "Not relevant for now"
            daily = DailyPref(date=date, shift_types=shift_types, constraints=constraints)
            wp.add_daily_preference(daily)
        return wp

    def add_first_pref(self, wp: WeeklyPref):
        data = wp.get_dict_format()
        self.collection.insert_one(data)

    def prepare_team_next_weekly_pref(self, team_id, wp: WeeklyPref):
        data = wp.get_dict_format()
        result = self.collection.update_many(
            {
                "TeamID": {"$eq": team_id}},
            {
                "$set": {
                    "ShiftID": data["ShiftID"],
                    "Dailies": data["Dailies"],
                    "StartDate": data["StartDate"],
                    "EndDate": data["EndDate"]
                }
            }
        )
    
    def update_employee_next_weekly_pref(self, employee_id, wp: WeeklyPref):
        data = wp.get_dict_format()
        result = self.collection.update_many(
            {
                "EmployeeID": {"$eq": employee_id}},
            {
                "$set": {
                    "Dailies": data["Dailies"],
                }
            }
        )

    def get_wp_from_doc(self, doc):
        employee_id = doc["EmployeeID"]
        team_id = doc["TeamID"]
        company_id = doc["CompanyID"]
        shift_id = doc["ShiftID"]
        wp = WeeklyPref(employee_id=employee_id, team_id=team_id, company_id=company_id, shift_id=shift_id)
        dailies = doc["Dailies"]
        for daily in dailies:
            date = daily["Date"]
            shift_for_obj = []
            shifts = daily["ShiftTypes"]
            for shift in shifts:
                if shift["Answer"] is False:
                    continue
                data = dict()
                data["StartHour"] = shift["StartHour"]
                data["EndHour"] = shift["EndHour"]
                data["ShiftName"] = shift["ShiftName"]
                shift_for_obj.append(data)
            daily_pref = DailyPref(date=date, shift_types=shift_for_obj)
            wp.add_daily_preference(dailypref=daily_pref)
        return wp

    def get_team_preferences(self, team_id):
        wpl = []
        query = {"TeamID": team_id}
        docs = self.collection.find(query, {})
        for doc in docs:
            wp = self.get_wp_from_doc(doc)
            wpl.append(wp)
        return wpl
    
    def get_employee_preferences(self, employee_id):
        wpl = []
        query = {"EmployeeID": employee_id}
        docs = self.collection.find(query, {})
        for doc in docs:
            wp = self.get_wp_from_doc(doc)
            wpl.append(wp)
        return wpl


# s = Shift(1, 1, 1, [{"ShiftName": "Evening", "StartHour": 1600, "EndHour": 2330, "NeededRoles":
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
# wph = WeeklyPrefHandler()
# wp = wph.derive_preferences_from_schedule(1, sc)
# wph.add_first_pref(wp=wp)
# wph.prepare_team_next_weekly_pref(team_id=7, wp=wp)
