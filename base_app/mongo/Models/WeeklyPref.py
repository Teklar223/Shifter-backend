from .DailyPref import DailyPref

class WeeklyPref:
    def __init__(self, employee_id, team_id, shift_id, company_id, dailies: list):
        self.__employee_id = employee_id
        self.__team_id = team_id
        self.__company_id = company_id
        self.__shift_id = shift_id
        self.__dailies = dailies

    def get_employee_id(self):
        return self.__employee_id

    def get_team_id(self):
        return self.__team_id

    def get_company_id(self):
        return self.__company_id

    def get_shift_id(self):
        return self.__shift_id

    def get_dailies(self):
        return self.__dailies

    def add_daily_preference(self, dailypref: DailyPref):
        self.__dailies.append(dailypref)

    def random_weekly_shifts(self):
        for i in range(len(self.__dailies)):
            self.__dailies[i].random_daily_shifts()

    def get_dict_format(self):
        output = {"EmployeeID": self.__employee_id, "TeamID": self.__team_id, "CompanyID": self.__company_id,
                  "ShiftID": self.__shift_id, "Dailies": []}
        for daily in self.__dailies:
            output["Dailies"].append(daily.get_dict_format())
        return output
