from bson import ObjectId
from base_app.mongo.Models.WeeklyPref import DailyPref, WeeklyPref
from base_app.mongo.Models.Schedule import Schedule
from base_app.mongo.Models.Shift import Shift
from base_app.mongo.Collection_Handler import CollectionHandler


class WeeklyPrefHandler(CollectionHandler):
    def __init__(self):
        CollectionHandler.__init__(self, "WeeklyPreferences")

    def derive_preferences_from_schedule(self, employee_id, role_id, schedule: Schedule, default_pref = False):
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
                
                # employee will receive weekly preferences only for its role.

                needed = available_shift["NeededRoles"]
                for needed_role in needed:
                    if needed_role.get("RoleID") is not None and needed_role.get("RoleID") == role_id:
                        shift_types.append(
                            {"StartHour": start_hour, "EndHour": end_hour, "ShiftName": shift_name, "Answer": answer})
                        # break
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
                }
            }
        )
    
    def update_employee_next_weekly_pref(self, employee_id, wp: WeeklyPref):
        data = wp.get_dict_format()
        query = {
                "EmployeeID": {"$eq": employee_id}
                # "EmployeeID": employee_id
        }
        to_update = {
                "$set": {
                    "Dailies": data["Dailies"],
                    "ShiftID": data["ShiftID"],
                    "TeamID": data["TeamID"],
                    "CompanyID": data["CompanyID"],
                    "EmployeeID": data["EmployeeID"]
                }
            }
        result = self.collection.find_one_and_update(query, to_update)
        # print("\n\n\n\n\n result\n\n\n\n\n\n")
        if result == None:
            print("\n\n\n\n\\n\n\nn HEREEEEEEEEEEEEEn\n\n\\n\n\n\n\n\n")
            self.add_first_pref(wp=wp)

    def get_wp_from_doc(self, doc):
        e_id = doc.get("EmployeeID")
        t_id = int(doc.get("TeamID"))
        c_id = int(doc.get("CompanyID"))
        s_id = doc.get("ShiftID")
        wp = WeeklyPref(employee_id=e_id, team_id=t_id, company_id=c_id, shift_id=s_id, dailies=[])
        dailies = doc.get("Dailies")
        for daily in dailies:
            date = int(daily.get("Date"))
            shift_for_obj = []
            shifts = daily.get("ShiftTypes")
            for shift in shifts:
                # if shift.get("Answer") is False:
                #     continue
                data = dict()
                data["StartHour"] = int(shift.get("StartHour"))
                data["EndHour"] = int(shift.get("EndHour"))
                data["ShiftName"] = shift.get("ShiftName")
                data["Answer"] = bool(shift.get("Answer"))
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
        doc = self.collection.find_one(query, {})
        wp = self.get_wp_from_doc(doc=doc)
        # for doc in docs:
        #     wp = self.get_wp_from_doc(doc)
        #     wpl.append(wp)
        return wp


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
