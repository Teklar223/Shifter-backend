from .AssignedDay import AssignedEvent, AssignedDay

class AssignedWeek:
    def __init__(self, start_date, end_date, shift_id, team_id, company_id, dailies: list = None):
        self.__shift_id = shift_id
        self.__team_id = team_id
        self.__company_id = company_id
        self.__start_date = start_date
        self.__end_date = end_date
        if dailies is None:
            self.__dailies = []
        else:
            self.__dailies = dailies

    # Getter methods
    def get_shift_id(self):
        return self.__shift_id

    def get_team_id(self):
        return self.__team_id

    def get_company_id(self):
        return self.__company_id

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def get_dailies(self):
        return self.__dailies

    # Setter methods
    def set_shift_id(self, shift_id):
        self.__shift_id = shift_id

    def set_team_id(self, team_id):
        self.__team_id = team_id

    def set_company_id(self, company_id):
        self.__company_id = company_id

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def set_end_date(self, end_date):
        self.__end_date = end_date

    def set_dailies(self, dailies):
        self.__dailies = dailies

    # TODO: Write a sort function by the date and add it to any addition function

    def add_daily_assignments(self, daily_assignment):
        if isinstance(daily_assignment, AssignedDay):
            self.__dailies.append(daily_assignment)

    def __add__(self, other):
        if isinstance(other, AssignedDay):
            self.add_daily_assignments(other)
        return self

    def replace_by_date(self, daily_assignments: AssignedDay):
        date = daily_assignments.get_date()
        if not (self.__start_date <= date <= self.__end_date):
            return
        idx = -1
        for i in range(len(self.__dailies)):
            if date == self.__dailies[i].get_date():
                idx = i
                break

        # If idx = -1, then we do not have such a daily assignment, so we will add it to the weekly assignment

        if idx == -1:
            self.add_daily_assignments(daily_assignment=daily_assignments)

        # Otherwise, replace the current daily assignment by the new one

        else:
            self.__dailies[i] = daily_assignments

    def __len__(self):
        return len(self.__dailies)

    def __iter__(self):
        return iter(self.__dailies)

    def get_dict_format(self):
        output = {"ShiftID": self.__shift_id, "TeamID": self.__team_id, "CompanyID": self.__company_id,
                  "StartDate": self.__start_date, "EndDate": self.__end_date}
        dailies = []
        for day in self.__dailies:
            dailies.append(day.get_dict_format())
        output["Dailies"] = dailies
        return output

    def __str__(self):
        return str(self.get_dict_format())
    
    def add_event(self, date: int, event: AssignedEvent):
        for day in self.__dailies:
            if day.get_date() == date:
                day += event

    # Static methods
    @classmethod
    def dict_to_week_obj(self, week_dict):
        shift_id = week_dict["ShiftID"]
        team_id = int(week_dict["TeamID"])
        company_id = int(week_dict["CompanyID"])
        start_date = int(week_dict["StartDate"])
        end_date = int(week_dict["EndDate"])
        week_assignment = AssignedWeek(start_date=start_date, end_date=end_date, shift_id=shift_id, team_id=team_id,
                                       company_id=company_id)
        for day_dict in week_dict["Dailies"]:
            day = AssignedDay.dict_to_day_object(day_dict)
            week_assignment += day
        return week_assignment
