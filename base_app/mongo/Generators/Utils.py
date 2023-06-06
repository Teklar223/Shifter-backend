import random
from ..Generators.GeneratorConstants import *
from ...mongo.Models.Schedule import Schedule, Shift

def get_random_working_hours():
    r = random.randint
    c = random.choice
    start_hour = r(0, 23)
    end_hour = r(0, 23)
    if start_hour > end_hour:
        temp = end_hour
        end_hour = start_hour
        start_hour = temp
    start_min = c(minutes)
    end_min = c(minutes)
    start_hour *= 100
    start_hour += start_min
    end_hour *= 100
    end_hour += end_min
    return start_hour, end_hour

def match_employee_role():
    output = []
    for i in employees:
        role = random.choice(roles)
        output.append({"EmployeeID": i, "RoleID": role})
    return output

def get_random_shift():
    start, end = get_random_working_hours()
    output = {"StartHour": start, "EndHour": end, "ShiftName": "Not Relevant"}
    taken_roles = [random.choice(roles)]
    role = random.choice(roles)
    while role in roles:
        role = random.choice(roles)
    taken_roles.append(role)
    needed_roles = []
    for role in taken_roles:
        count = random.randint(1, 5)
        needed_roles.append({"RoleID": role, "NeededWorkers": count})
    output["NeededRoles"] = needed_roles
    return output