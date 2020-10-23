class Action():
    def __init__(self, name: str) -> None:
        self._name = name
        self._precondition = ""

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name:str) -> None:
        self._name = name

    @property
    def precondition(self) -> str:
        return self._precondition

    @precondition.setter
    def preconditions(self, preconditions: str) -> None:
        self._precondition = preconditions

    def setEffect(self, effect: dict) -> str:
        pass

    def __str__(self):
        return f"Action: {self.name} \t\nPrecondition: {self.preconditions}"
