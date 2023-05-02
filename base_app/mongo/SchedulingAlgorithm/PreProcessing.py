from pprint import pprint
from ..Models.WeeklyPref import DailyPref, WeeklyPref
from ..Models.Schedule import Schedule, Shift
from ..WeeklyPref_Handler import WeeklyPrefHandler
from ..Shifts_Handler import Shifts_Handler

"""
This function will get a document from Shifts collection and derive it into a template that we will later use
in the scheduling algorithm.
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
            workers = shift["NeededRoles"][0]["NeededWorkers"]
            role_id = shift["NeededRoles"][0]["RoleID"]
            template.get(daily.get_date()).append(
                {"StartHour": start_hour, "EndHour": end_hour, "Workers": workers, "RoleID": role_id})
            roles.add(role_id)
    return template, roles, team_id


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
        for shift in data:
            start_hour = shift["StartHour"]
            end_hour = shift["EndHour"]
            workers = shift["Workers"]
            role_id = shift["RoleID"]
            template_by_role[role_id][date].append({"StartHour": start_hour, "EndHour": end_hour, "Workers": workers})
    return template_by_role


# TODO: check the function


def derive_preferences_template_from_wp(wp: WeeklyPref):
    template = wp.get_dict_format()
    template.pop("TeamID")
    template.pop("ShiftID")
    template.pop("CompanyID")
    return template


# TODO: check the function


def derive_preferences_template_by_team_id(team_id):
    wph = WeeklyPrefHandler()
    output = []
    wp_list = wph.get_team_preferences(team_id=team_id)
    for wp in wp_list:
        output.append(derive_preferences_template_from_wp(wp))
    return wp_list

# pp = pprint.PrettyPrinter(indent=4)
pprint(derive_template_for_scheduling('643db236077a1bb573e4339a')[0], width=10, depth=6)
# print(divide_template_by_role_id('643db236077a1bb573e4339a'))
# print(derive_template_for_scheduling('643db236077a1bb573e4339a')[0][1])