from datetime import date, timedelta

def today_to_int_format():
    return date_to_int_format(date.today())

def date_to_int_format(date):
    d = date.day
    m = date.month
    y = date.year
    if d < 10:
        d = f"0{d}"
    else:
        d = f"{d}"
    if m < 10:
        m = f"0{m}"
    else:
        m = f"{m}"
    y = f"{y}"
    date = f"{y}{m}{d}"
    return int(date)
    
def next_week_to_int_format():
    next = date.today() + timedelta(days=7)
    return date_to_int_format(next)

def get_date_week_difference_to_int_format(date, week_number: int):
    delta = week_number * 7
    return date + timedelta(days=delta)
