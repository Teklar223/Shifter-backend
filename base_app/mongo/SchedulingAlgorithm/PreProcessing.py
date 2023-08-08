from pprint import pprint
# from base_app.mongo.Models.Schedule import Schedule, Shift
from base_app.mongo.WeeklyPref_Handler import WeeklyPrefHandler
from base_app.mongo.Shifts_Handler import Shifts_Handler
from base_app.mongo.Models.WeeklyPref import DailyPref, WeeklyPref


"""
This function will get a document from Shifts collection and derive it into a template that
we will later use in the scheduling algorithm.
"""


def derive_template_for_scheduling(shift_id):
    sh = Shifts_Handler()
    sc = sh.get_schedule_by_shift_id(shift_id=shift_id)
    team_id = sc.get_team_id()
    template = dict()
    roles = set()
    for daily in sc.get_daily_shifts():
        template[daily.get_date()] = []
        for shift in daily.get_available_shifts():
            start_hour = shift["StartHour"]
            end_hour = shift["EndHour"]
            shift_name = shift["ShiftName"]
            for workers_data in shift["NeededRoles"]:
                workers = workers_data["NeededWorkers"]
                role_id = workers_data["RoleID"]
                template.get(daily.get_date()).append(
                    {"StartHour": start_hour, "EndHour": end_hour, "ShiftName": shift_name, "Workers": workers, "RoleID": role_id})
                roles.add(role_id)
    return template, roles, team_id, sc


"""
This function will get a template and roles as input and. It will divide the template into 
templates by the roles so the algorithm can run on each role separately.
"""


def divide_scheduling_template_by_role_id(template, roles):
    template_by_role = dict()
    for role_id in roles:
        template_by_role[role_id] = dict()
        for date in template.keys():
            template_by_role[role_id][date] = []
    for date, data in template.items():
        can_work = False
        for shift in data:
            start_hour = shift["StartHour"]
            end_hour = shift["EndHour"]
            workers = shift["Workers"]
            role_id = shift["RoleID"]
            shift_name = shift["ShiftName"]
            can_work = True
            template_by_role[role_id][date].append({"StartHour": start_hour, "EndHour": end_hour, "ShiftName":shift_name, "Workers": workers})
    if not can_work:
        template_by_role[role_id].pop(date)
    return template_by_role


# TODO: check the function


def derive_preferences_template_from_wp(wp: WeeklyPref):
    template = wp.get_dict_format()
    template.pop("TeamID")
    template.pop("ShiftID")
    template.pop("CompanyID")
    return template


# TODO: check the function


def derive_preferences_template_by_team_id(team_id, date):
    wph = WeeklyPrefHandler()
    output = []
    wp_list = wph.get_team_preferences(team_id=team_id, date=date)
    for wp in wp_list:
        output.append(derive_preferences_template_from_wp(wp))
    return output

def divide_employees_by_role(wp_list: list, roles, employees_roles):
    wp_dict = dict()
    for role in roles:
        wp_dict[role] = []
    for wp in wp_list:
        role = employees_roles.get(wp.get("EmployeeID"))
        wp_dict.get(role).append(wp)
    return wp_dict

"""
PreProcessing Algorithms:
Input: ShiftID, dictionary from employees in the team to their roles.
Output: Scheduling templates dictinary divided by roles,
        Weekly preferences templates divided by roles,
        set of roles
    1. derive the template for the scheduling algorithm
    2. divide the template to multiple templates by the roles to create template for each role
    3. get all the weekly preferences of the entire team using the team_id recieves in stage 1.
    4. divide the preferences templates by the roles of the employees.
    5. return the scheduling template and wp template divided by role and the set of roles


"""

def preprocessing(shift_id: str, employees_roles:dict, date: int):
    template, roles, team_id, sc = derive_template_for_scheduling(shift_id=shift_id)
    template_by_role = divide_scheduling_template_by_role_id(template, roles)
    wp_list = derive_preferences_template_by_team_id(team_id=team_id, date=date)    
    wp_template_by_role = divide_employees_by_role(wp_list=wp_list, roles=roles, employees_roles=employees_roles)
    return template_by_role, wp_template_by_role, roles, sc

# pp = pprint.PrettyPrinter(indent=4)
# pprint(derive_template_for_scheduling('643db236077a1bb573e4339a')[0], width=10, depth=6)
# print(divide_template_by_role_id('643db236077a1bb573e4339a'))
# print(derive_template_for_scheduling('643db236077a1bb573e4339a')[0][1])