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