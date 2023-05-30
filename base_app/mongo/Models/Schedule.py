from .Shift import Shift


class Schedule:
    '''
        'weekly' schedule (start and end dates can vary and dont have to be exactly a week)
    '''
    def __init__(self, company_id, team_id, startdate, enddate, shift_id=None):
        self.company_id = company_id
        self.team_id = team_id
        self.start_date = startdate
        self.end_date = enddate
        self.shift_id = shift_id
        self.daily_shifts = []

    def add_shift(self, shift):
        self.daily_shifts.append(shift)

    def get_company_id(self):
        return self.company_id

    def get_team_id(self):
        return self.team_id

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_shift_id(self):
        return self.shift_id

    def get_daily_shifts(self):
        return self.daily_shifts

    def get_dict_format(self):
        s_dict = {"CompanyID": self.company_id, "TeamID": self.team_id,
                  "StartDate": self.start_date, "EndDate": self.end_date, "DailyShifts": [x.get_dict_format() for x in self.daily_shifts]}
        if self.shift_id is None:
            s_dict["ShiftID"] = "None"
        else:
            s_dict["ShiftID"] = self.shift_id
        return s_dict

    def add_daily_shift(self, shift: Shift):
        self.daily_shifts.append(shift)


