from base_app.mongo.SchedulingAlgorithm.Tuple_Key import Tuple_Key
from .strategies_constants import *
from .HourStrategies.MaxHoursSchedule import Max_Hour_Schedule_Strategy
from .HourStrategies.MaxHoursStrategy import Max_Hour_Daily_Strategy

def get_strategies(strategies_dict: dict, shift_keys):
    strategies = []
    for strategy, demands in strategies_dict.items():
        for demand in demands:
            new_strategy = None
            if strategy == max_hours_per_date_employee:
                new_strategy = Max_Hour_Daily_Strategy(
                    input_keys=demand, keys=shift_keys)
            elif strategy == max_hours_per_schedule_employee:
                new_strategy = Max_Hour_Schedule_Strategy(
                    input_keys=demand, keys=shift_keys)
            if new_strategy is not None:
                strategies.append(new_strategy)
    return strategies


def divide_strategies_by_role(strategies_dict: dict, employees_roles: dict, roles: set):
    strategies_roles = dict()
    for role in roles:
        strategies_roles[role] = dict()
    strategies_global = dict()
    for strategy, demands in strategies_dict.items():
        # first condition: then its not global since we need to apply more than one strategies
        # second condition: then there is only one employee which we need to apply the strategy on
        if (isinstance(demands, list)) and (strategy in role_dependany_strategies_list):
            for demand in demands:
                employee_id = demand["EmployeeID"]
                role_id = employees_roles.get(employee_id)
                if role_id is None:
                    raise TypeError("No such employee")
                if strategies_roles.get(role_id).get(strategy) is None:
                    strategies_roles.get(role_id)[strategy] = []
                strategies_roles.get(role_id).get(strategy).append(demand)
        elif (isinstance(demands, dict)) and (strategy in role_dependany_strategies_list):
            employee_id = demands["EmployeeID"]
            role_id = employees_roles.get(employee_id)
            if role_id is None:
                raise TypeError("No such employee")
            if strategies_roles.get(role_id).get(strategy) is None:
                strategies_roles.get(role_id)[strategy] = []
            strategies_roles.get(role_id).get(strategy).append(demands)
        else:
            if (isinstance(demands, list)) and (strategy in global_strategies_list):
                for demand in demands:
                    if strategies_global.get(strategy) is None:
                        strategies_global[strategy] = []
                    strategies_global.get(strategy).append(demand)
            elif (isinstance(demands, dict)) and (strategy in global_strategies_list):
                if strategies_global.get(strategy) is None:
                        strategies_global[strategy] = []
                strategies_global.get(strategy).append(demands)
            else:
                if len(demands) > 0:
                    raise TypeError(f"Unknown strategy:\t {strategy}")
    return strategies_roles, strategies_global
