from copy import deepcopy

def get_maximal_workers_dict(shift_template: dict):
    output = dict()
    for date, shifts in shift_template.items():
        output[date] = dict()
        for shift in shifts:
            _, shift_str = get_shift_str(shift, "Workers")
            max_workers = shift.get("Workers")
            output.get(date)[shift_str] = max_workers
    return output


def get_shift_str(shift, item):
     shift_copy = deepcopy(shift)
     shift_copy.pop(item)
     return shift_copy, str(shift_copy)

def transform(input: list):
    numbers = range(len(input))
    output = dict()
    for i in input:
        pass

def isIntersect(key1, key2):
    if key1.get_employee_id() != key2.get_employee_id():
        return False
    if key1.get_date() != key2.get_date():
        return False
    data_key1 = key1.get_data()
    data_key2 = key2.get_data()
    start_key1 = data_key1.get("StartHour")
    end_key1 = data_key1.get("EndHour")
    start_key2 = data_key2.get("StartHour")
    end_key2 = data_key2.get("EndHour")
    if (start_key1 < start_key2 < end_key1) or (start_key1 < end_key2 < end_key1):
        return True
    elif (start_key2 < start_key1 < end_key2) or (start_key2 < end_key1 < end_key2):
        return True
    return False