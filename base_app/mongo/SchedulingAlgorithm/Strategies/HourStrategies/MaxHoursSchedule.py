from base_app.mongo.SchedulingAlgorithm.Strategies.Stratrgy import Strategy
from ortools.sat.python import cp_model
from base_app.mongo.SchedulingAlgorithm.Strategies.HourStrategies.TimeUtils import calculate_hours

"""
This class is the strategy to limit the maximum working per week for given employees
"""

class Max_Hour_Schedule_Strategy(Strategy):
    def __init__(self, keys, input_keys):
        Strategy.__init__(self, shift_keys=keys, input_keys=input_keys)


    def execute(self, model, shifts: dict):
        emplyee_id = self._input_keys.get("EmployeeID")
        max_hours = self._input_keys.get("MaxHours") * 3600

        """
        Take only the shifts that of the given employee in the given date
        """

        needed_keys = [x for x in list(filter(lambda obj: obj.get_employee_id() == emplyee_id, self._keys))]
        if len(needed_keys) == 0:
            return model
        
        working_time = []
        for key in needed_keys:
            # the nubmer of seconds the employee worked * (1 - the employee worked/0 - the employee does not worked)
            working_time.append(shifts[key] * calculate_hours(key=key).seconds)
        model.Add(sum(working_time) <= max_hours)
        return model

