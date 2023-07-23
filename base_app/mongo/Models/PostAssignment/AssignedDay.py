from .AssignedEvent import AssignedEvent

class AssignedDay:
    def __init__(self, date, start_hour, end_hour, events: list = None):
        self.__date = date
        self.__start_hour = start_hour
        self.__end_hour = end_hour
        if events is None:
            self.__events = []
        else:
            self.__events = events

    # Getter methods
    def get_date(self):
        return self.__date

    def get_start_hour(self):
        return self.__start_hour

    def get_end_hour(self):
        return self.__end_hour

    def get_events(self):
        return self.__events

    # Setter methods
    def set_date(self, date):
        self.__date = date

    def set_start_hour(self, start_hour):
        self.__start_hour = start_hour

    def set_end_hour(self, end_hour):
        self.__end_hour = end_hour

    def set_events(self, events):
        self.__events = events

    def add_event_object(self, event):
        if isinstance(event, AssignedEvent):
            self.__events.append(event)
        return

    def add_event_parameters(self, starthour, endhour, employee_id):
        event = AssignedEvent(start_hour=starthour, end_hour=endhour, employee_id=employee_id)
        self.__events.append(event)

    def __len__(self):
        return len(self.__events)

    def __iter__(self):
        return iter(self.__events)

    def __add__(self, other):
        if isinstance(other, AssignedEvent):
            self.__events.append(other)
        return self


    def get_dict_format(self):
        output = {"Date": self.__date, "StartHour": self.__start_hour, "EndHour": self.__end_hour}
        events = []
        for event in self.__events:
            events.append(event.get_dict_format())
        output["Shifts"] = events
        return output

    def __str__(self):
        return str(self.get_dict_format())

    # Static Metods
    @classmethod
    def dict_to_day_object(self, dict_obj: dict):
        start_hour = int(dict_obj["StartHour"])
        end_hour = int(dict_obj["EndHour"])
        date = int(dict_obj["Date"])
        day = AssignedDay(date=date, start_hour=start_hour, end_hour=end_hour)
        for event_dict in dict_obj["Shifts"]:
            event = AssignedEvent.dict_to_event_obj(event_dict)
            day += event
        return day

# e1 = AssignedEvent(900, 1200, 1)
# e2 = AssignedEvent(1200, 1700, 2)
# d = AssignedDay(20230430, 900, 1700)
# d = d + e1
# d += e2
# print(d)