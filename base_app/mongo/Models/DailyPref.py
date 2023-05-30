class DailyPref:
    def __init__(self, date: int , shift_types: list, constraints=None):
        self.__date = date
        # Format: list of {"ShiftType": "Morning", "StartHour": starthour, "EndHour": endhour, "Answer": answer
        self.__shift_types = shift_types
        self.__constraints = constraints


    def get_date(self):
        return self.__date

    def get_shift_types(self):
        return self.__shift_types

    def get_constraints(self):
        return self.__constraints

    def set_can_work(self, shift_title, answer):
        for i in range(len(self.__shift_types)):
            if self.__shift_types[i]["ShiftType"] == shift_title:
                self.__shift_types[i]["Answer"] = answer
                return

    def get_dict_format(self):
        output = {"Date": self.__date}
        output["ShiftTypes"] = self.__shift_types
        output["Constraints"] = self.__constraints
        return output



