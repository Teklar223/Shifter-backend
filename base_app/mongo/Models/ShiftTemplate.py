class Shift_Template:
    def __init__(self, team_id: int, template_name: str, start_hour: int, end_hour: int, needed_roles: list, template_id: str = None) -> None:
        self.__team_id = team_id
        self.__template_name = template_name
        self.__start_hour = start_hour
        self.__end_hour = end_hour
        self.__needed_roles = needed_roles
        if template_id is None:
            self.__template_id = "None"
        else:
            self.__template_id = template_id

    def get_template_name(self) -> str:
        return self.__template_name
    
    def set_template_name(self, template_name: str) -> None:
        self.__template_name = template_name
    
    def get_start_hour(self) -> int:
        return self.__start_hour
    
    def set_start_hour(self, start_hour: int) -> None:
        self.__start_hour = start_hour
    
    def get_end_hour(self) -> int:
        return self.__end_hour
    
    def set_end_hour(self, end_hour: int) -> None:
        self.__end_hour = end_hour
    
    def get_needed_roles(self) -> list:
        return self.__needed_roles
    
    def set_needed_roles(self, needed_roles: list) -> None:
        self.__needed_roles = needed_roles

    def get_team_id(self):
        return self.__team_id
    
    def get_template_id(self):
        return self.__template_id
    
    def serialize(self):
        template_dict = {"TemplateID": self.__template_id, "TeamID": self.__team_id,
                "TemplateName": self.__template_name, "StartHour": self.__start_hour,
                  "EndHour": self.__end_hour, "NeededRoles": self.__needed_roles}
        return template_dict
    
    # Static methods
    @classmethod
    def deserialize(self, template_dict):
        template_id = template_dict["TemplateID"]
        team_id = template_dict["TeamID"]
        template_name = template_dict["TemplateName"]
        start_hour = template_dict["StartHour"]
        end_hour = template_dict["EndHour"]
        needed_roles = template_dict["NeededRoles"]
        template = Shift_Template(team_id=team_id, template_name=template_name,
                                   start_hour=start_hour, end_hour=end_hour,
                                     needed_roles=needed_roles, template_id=template_id)
        return template