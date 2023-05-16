# from base_app.mongo.Models.PostAssignment import *
# from base_app.mongo.Shifts_Handler import Shifts_Handler
# from base_app.mongo.AssignmentsHandler import Assignment_Handler
import os
from base_app.mongo.Models.PostAssignment.AssignedDay import AssignedDay
from base_app.mongo.SchedulingAlgorithm.PreProcessing import *
from base_app.mongo.Models.PostAssignment.AssignedEvent import AssignedEvent
from base_app.mongo.Models.PostAssignment.AssignedWeek import AssignedWeek
from base_app.mongo.SchedulingAlgorithm.Tuple_Key import Tuple_Key
# from base_app.mongo.SchedulingAlgorithm.Algorithm import schedule

os.environ["MONGO_URI"] = "'mongodb+srv://Unusual55:Poserkiller55@cluster0.uadle.mongodb.net/test'"

# print(f"{os.environ.set('MONGO_URI')}")
sh = Shifts_Handler()
sc = sh.get_schedule_by_shift_id('643db236077a1bb573e4339a')
print(sc.get_dict_format())


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
# a, b, c = preprocessing(shift_id='643db236077a1bb573e4339a', employees_roles=emp)
# input_keys = {"EmployeeID": 1, "Date": 1, "MaxHours": 12}
# input_keys2 = {"EmployeeID": 1, "MaxHours": 30}
# input_strategies = {"MAX_HOURS_EMPLOYEE_DAILY": input_keys,
                    # "MAX_HOURS_EMPLOYEE_SCHEDULE": input_keys2}
# output = schedule(shift_id='643db236077a1bb573e4339a',
                #   employee_roles=emp, strategies=input_strategies)
# print(11111)
# print(a)
# print(b)
# print(c)
