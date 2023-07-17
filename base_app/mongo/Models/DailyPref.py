import random


class DailyPref:
    def __init__(self, date: int , shift_types: list, constraints=None):
        self.__date = date
        # Format: list of {"ShiftType": "Morning", "StartHour": starthour, "EndHour": endhour, "Answer": answer
        self.__shift_types = shift_types
        self.__constraints = constraints
        self.__parse_shift_types()


    def __parse_shift_types(self):
        for i in range(len(self.__shift_types)):
            self.__shift_types[i]["StartHour"] = int(self.__shift_types[i].get("StartHour"))
            self.__shift_types[i]["StartHour"] = int(self.__shift_types[i].get("EndHour"))
            answer = self.__shift_types[i].get("Answer")
            if answer == "true".lower:
                answer = True
            else:
                answer = False
            self.__shift_types[i]["Answer"] = answer




    def get_date(self):
        return self.__date
    
    def random_daily_shifts(self):
        for i in range(len(self.__shift_types)):
            coin = random.randint(0, 9)
            if coin <= 6:
                self.__shift_types[i]["Answer"] = True

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




