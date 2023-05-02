class AssignedEvent:
    def __init__(self, start_hour, end_hour, employee_id):
        self.__start_hour = start_hour
        self.__end_hour = end_hour
        self.__employee_id = employee_id

    # Getter methods
    def get_start_hour(self):
        return self.__start_hour

    def get_end_hour(self):
        return self.__end_hour

    def get_employee_id(self):
        return self.__employee_id

    # Setter methods
    def set_start_hour(self, start_hour):
        self.__start_hour = start_hour

    def set_end_hour(self, end_hour):
        self.__end_hour = end_hour

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_dict_format(self):
        return {"StartHour": self.__start_hour, "EndHour": self.__end_hour, "EmployeeID": self.__employee_id}

    def __str__(self):
        return str(self.get_dict_format())


    # Static Functions
    @classmethod
    def dict_to_event_obj(dict_obj: dict):
        start_hour = dict_obj["StartHour"]
        end_hour = dict_obj["EndHour"]
        employee_id = dict_obj["Employee_id"]
        return AssignedEvent(start_hour=start_hour, end_hour=end_hour, employee_id=employee_id)