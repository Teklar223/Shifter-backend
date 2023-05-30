class Strategy:
    def __init__(self, shift_keys: set, input_keys: set) -> None:

        self._keys = shift_keys
        self._input_keys = input_keys

    def execute(self, model, shifts: dict):
        raise NotImplementedError("You need to use this function from one of the classes that inherit this class")
    