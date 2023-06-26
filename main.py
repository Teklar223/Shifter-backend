# from base_app.mongo.Models.PostAssignment import *
# from base_app.mongo.Shifts_Handler import Shifts_Handler
# from base_app.mongo.AssignmentsHandler import Assignment_Handler
import os
from base_app.mongo.Models.PostAssignment.AssignedDay import AssignedDay
from base_app.mongo.SchedulingAlgorithm.PreProcessing import *
from base_app.mongo.Models.PostAssignment.AssignedEvent import AssignedEvent
from base_app.mongo.Models.PostAssignment.AssignedWeek import AssignedWeek
from base_app.mongo.SchedulingAlgorithm.Tuple_Key import Tuple_Key
from base_app.mongo.SchedulingAlgorithm.Algorithm import schedule
from base_app.mongo.Models.ShiftTemplate import Shift_Template
from base_app.mongo.Models.Schedule import Shift, Schedule
from base_app.mongo.Models.WeeklyPref import DailyPref, WeeklyPref
from base_app.mongo.AssignmentsHandler import Assignment_Handler

os.environ["MONGO_URI"] = "'mongodb+srv://Unusual55:Poserkiller55@cluster0.uadle.mongodb.net/test'"

# print(f"{os.environ.set('MONGO_URI')}")
# sh = Shifts_Handler()
# sc = sh.get_schedule_by_shift_id('643db236077a1bb573e4339a')
# print(sc.get_dict_format())


# e1 = AssignedEvent(1000, 1200, 1)
# e2 = AssignedEvent(1100, 1900, 3)
# d1 = AssignedDay(20230505, 1000, 1900)
# d1 += e1
# d1 += e2
# e3 = AssignedEvent(800, 1200, 2)
# e4 = AssignedEvent(1200, 1900, 1)
# d2 = AssignedDay(20230506, 800, 1900)
# d2 += e3
# d2 += e4
# w = AssignedWeek(start_date=20230505, end_date=20230508, shift_id='643db236077a1bb573e4339a', team_id=7, company_id=9)
# w += d1
# w += d2


# ash = Assignment_Handler()
# assignment = ash.get_assignment_by_shift_id('643db236077a1bb573e4339a')
# print(assignment.get_dict_format())
# ash.add_new_assignment(w)

# out = ash.get_recent_assignments_by_team_id(team_id=7, count=2)
# for i in out:
#     print(i.get_dict_format())

# emp = {1: 1500, 2: 1510}
# a, b, c, sc = preprocessing(shift_id='643db236077a1bb573e4339a', employees_roles=emp)
# input_keys = {"EmployeeID": 1, "Date": 1, "MaxHours": 12}
# input_keys2 = {"EmployeeID": 1, "MaxHours": 30}
# input_strategies = {"MAX_HOURS_EMPLOYEE_DAILY": input_keys,
#                     "MAX_HOURS_EMPLOYEE_SCHEDULE": input_keys2}
# print(input_strategies)
# output = schedule(shift_id='643db236077a1bb573e4339a',
#                   employee_roles=emp, strategies=input_strategies)
# print(output)
# print(11111)
# print(a)
# print(b)
# print(c)

# handler = WeeklyPrefHandler()
# wp = handler.get_employee_preferences(1)
# print(wp.get_dict_format())

# t = {
#     "TemplateID": 1,
#     "TeamID": 1,
#     "TemplateName": "Morning A",
#     "StartHour": 800,
#     "EndHour": 1900,
#     "NeededRoles": [
#         {
#             "RoleID": 1,
#             "NeededWorkers": 3
#         },
#         {
#             "RoleID": 2,
#             "NeededWorkers": 1
#         },
#         {
#             "RoleID": 3,
#             "NeededWorkers": 2
#         },
#     ]
# }
# template = Shift_Template.deserialize(t)
# print(template.serialize())
# print(os.environ.get("MONGO_URI")[1:-1])
# regular_morning = {
#                     "ShiftName": "Morning",
#                     "StartHour": 800,
#                     "EndHour": 1600,
#                     "NeededRoles": [
#                         {
#                             "RoleID": 1,
#                             "NeededWorkers": 2
#                         },
#                         {
#                             "RoleID": 2,
#                             "NeededWorkers": 1
#                         },
#                         {
#                             "RoleID": 3,
#                             "NeededWorkers": 1
#                         }
#                     ]
#                 }
# regular_middle = {
#                     "ShiftName": "Middle",
#                     "StartHour": 1200,
#                     "EndHour": 2000,
#                     "NeededRoles": [
#                         {
#                             "RoleID": 1,
#                             "NeededWorkers": 1
#                         }
#                     ]
#                 }
# regular_evening = {
#                     "ShiftName": "Evening",
#                     "StartHour": 1600,
#                     "EndHour": 2023,
#                     "NeededRoles": [
#                         {
#                             "RoleID": 1,
#                             "NeededWorkers": 2
#                         },
#                         {
#                             "RoleID": 2,
#                             "NeededWorkers": 1
#                         },
#                         {
#                             "RoleID": 3,
#                             "NeededWorkers": 1
#                         }
#                     ]
#                 }

# weekend_morning = {
#                     "ShiftName": "Friday Morning",
#                     "StartHour": 800,
#                     "EndHour": 1400,
#                     "NeededRoles": [
#                         {
#                             "RoleID": 1,
#                             "NeededWorkers": 2
#                         },
#                         {
#                             "RoleID": 2,
#                             "NeededWorkers": 1
#                         },
#                         {
#                             "RoleID": 3,
#                             "NeededWorkers": 1
#                         }
#                     ]
#                 }

# weekend_mid = {
#                     "ShiftName": "Friday Middle",
#                     "StartHour": 1100,
#                     "EndHour": 1500,
#                     "NeededRoles": [
#                         {
#                             "RoleID": 1,
#                             "NeededWorkers": 1
#                         }
#                     ]
#                 }

# weekend_closure = {
#                     "ShiftName": "Friday Closure",
#                     "StartHour": 1200,
#                     "EndHour": 1700,
#                     "NeededRoles": [
#                         {
#                             "RoleID": 1,
#                             "NeededWorkers": 2
#                         },
#                         {
#                             "RoleID": 2,
#                             "NeededWorkers": 1
#                         },
#                         {
#                             "RoleID": 3,
#                             "NeededWorkers": 1
#                         }
#                     ]
#                 }

# regular = [regular_morning, regular_middle, regular_evening]
# weekend = [weekend_morning, weekend_mid, weekend_closure]

# sunday = Shift(date=20230611, starthour=800, endhour=2300, possible_shifts=regular)
# monday = Shift(date=20230612, starthour=800, endhour=2300, possible_shifts=regular)
# tuesday = Shift(date=20230613, starthour=800, endhour=2300, possible_shifts=regular)
# wednsday = Shift(date=20230614, starthour=800, endhour=2300, possible_shifts=regular)
# thursday = Shift(date=20230615, starthour=800, endhour=2300, possible_shifts=regular)
# friday = Shift(date=20230616, starthour=800, endhour=1700, possible_shifts=weekend)
# sc = Schedule(company_id=7, team_id=5, startdate=20230611, enddate=20230616, shift_id='64805c7e5dbea67698ce9dc2')
# sc.add_daily_shift(sunday)
# sc.add_daily_shift(monday)
# sc.add_daily_shift(tuesday)
# sc.add_daily_shift(wednsday)
# sc.add_daily_shift(thursday)
# sc.add_daily_shift(friday)

# # handler = Shifts_Handler()
# # handler.add_new_shift(sc)


"""
Create random shifts
"""
# employees = {"host1@gmail.com": 3, "host2@gmail.com": 3, "host3@gmail.com": 3, "waiter1@gmail.com": 1, "waiter2@gmail.com": 1, "waiter3@gmail.com": 1, "waiter4@gmail.com": 1, "waiter5@gmail.com": 1, "waiter6@gmail.com": 1, "shitftmanager1@gmail.com": 2, "shitftmanager2@gmail.com": 2, "shitftmanager3@gmail.com": 2}
# shift_handler = Shifts_Handler()
# sc = shift_handler.get_schedule_by_shift_id(shift_id='64805c7e5dbea67698ce9dc2')
# handler = WeeklyPrefHandler()
# wp_list = []
# for employee in employees:
#     wp = handler.derive_preferences_from_schedule(employee_id=employee, schedule=sc)
#     wp_list.append(wp)

# for i in range(len(wp_list)):
#     wp_list[i].random_weekly_shifts()

# for wp in wp_list:
#     handler.update_employee_next_weekly_pref(employee_id=wp.get_employee_id(), wp=wp)

emp = {"host1@gmail.com": 3, "host2@gmail.com": 3, "host3@gmail.com": 3, "waiter1@gmail.com": 1, "waiter2@gmail.com": 1, "waiter3@gmail.com": 1, "waiter4@gmail.com": 1, "waiter5@gmail.com": 1, "waiter6@gmail.com": 1, "shitftmanager1@gmail.com": 2, "shitftmanager2@gmail.com": 2, "shitftmanager3@gmail.com": 2}

# emp = {1: 1500, 2: 1510}
a, b, c, sc = preprocessing(shift_id='64805c7e5dbea67698ce9dc2', employees_roles=emp)
input_keys = {"EmployeeID": "host1@gmail.com", "Date": 20230613, "MaxHours": 8}
input_keys2 = {"EmployeeID": "host1@gmail.com", "MaxHours": 40}
input_strategies = {"MAX_HOURS_EMPLOYEE_DAILY": [input_keys],
                    "MAX_HOURS_EMPLOYEE_SCHEDULE": [input_keys2]}
# print(input_strategies)
# output = schedule(shift_id='64805c7e5dbea67698ce9dc2',
                #   employee_roles=emp, strategies=input_strategies)
# print(output)


# handler = Assignment_Handler()
# data = handler.get_bounded_dated_assignments_by_team_id(team_id=5, start_date=20230601, end_date=20230630)
# print(data)

handler = Shifts_Handler()
data = handler.get_dated_shift_by_team_id(team_id=5, date=20230611)
print(data.get_dict_format())