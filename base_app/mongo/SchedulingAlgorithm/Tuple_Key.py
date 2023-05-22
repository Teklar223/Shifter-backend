class Tuple_Key:
    def __init__(self, employee_id: int, date: int, shift: str) -> None:
        self.__employee_id = employee_id
        self.__date = date
        self.__shift = str(shift)
        self.__data = shift

    def get_employee_id(self):
        return self.__employee_id
    
    def get_date(self):
        return self.__date
    
    def get_shift(self):
        return self.__shift
    
    def get_data(self):
        return self.__data
    
    def __str__(self) -> str:
        return str(f'EmployeeID: {self.__employee_id}\t Date: {self.__date}\t Shift: {self.__shift}')
    
    def __repr__(self) -> str:
        return str(self)
    
    def __hash__(self) -> int:
        return hash(str(self))
    
    def __eq__(self, __value: object) -> bool:
        return self.__employee_id == __value.__employee_id and self.__date == __value.__date and self.__shift == __value.__shift