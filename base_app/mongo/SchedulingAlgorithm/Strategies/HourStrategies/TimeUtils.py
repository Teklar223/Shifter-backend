from datetime import datetime
from ...Tuple_Key import Tuple_Key
def time_string_format(input: int):
    minutes = str(input)[-2:]
    hours = str(input)[:-2]
    seconds = str("00")
    return str(f'{hours}:{minutes}:{seconds}')


def calculate_hours(key: Tuple_Key):
    data = key.get_data()
    start = data.get("StartHour")
    end = data.get("EndHour")
    start_hour = time_string_format(start)
    start_time = datetime.strptime(start_hour, "%H:%M:%S")
    end_hour = time_string_format(end)
    end_time = datetime.strptime(end_hour, "%H:%M:%S")
    return abs(end_time - start_time)