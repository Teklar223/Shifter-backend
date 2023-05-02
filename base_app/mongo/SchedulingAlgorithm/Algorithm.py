from ortools.sat.python import cp_model
from Objects.SchedulingAlgorithm.PreProcessing import derive_preferences_template_from_wp, \
    derive_template_for_scheduling, divide_scheduling_template_by_role_id, derive_preferences_template_by_team_id


# TODO: update maximum hours per day
# Assuming that I get a dictionary from employee_id to role_id, seperate by roles and run the algorithm seperately

def initialize_cp_model(shift_id, maximum_hours_per_day):
    shift_template, roles, team_id = derive_template_for_scheduling(shift_id=shift_id)
    shift_template_role = divide_scheduling_template_by_role_id(shift_template, roles)
    wp_list = derive_preferences_template_by_team_id(team_id=team_id)

