class Shift:
    def __init__(self, date, starthour, endhour, possible_shifts):
        self.date = date
        self.start_hour = starthour
        self.end_hour = endhour
        self.available = possible_shifts

    def get_date(self):
        return self.date

    def get_start_hour(self):
        return self.start_hour

    def get_end_hour(self):
        return self.end_hour

    def get_available_shifts(self):
        return self.available

    def get_dict_format(self):
        s_dict = {"Date": self.date, "StartHour": self.start_hour, "EndHour": self.end_hour,
                  "PossibleShifts": self.available}
        return s_dict
