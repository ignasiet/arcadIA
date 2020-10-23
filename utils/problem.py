from utils.config import ConfigFile
from .action import Action
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional

class Problem():
    def __init__(self):
        # self.name = config.name
        # self.actions = []
        # self.actions.extend(self.parseActions(config.actions))
        self._types = {}
        self._vars2pos = {}
        self.actions = []
        self.initialstate = []
        self.goalTest = ""

    def __str__(self):
        return f"Types: {self.types} \nVars: {self.vars2pos} \nInitial state: {self.initialstate} \nGoal: {self.goalTest} \nActions:\n{[a for a in self.actions]}"

    @property
    def types(self) -> dict:
        return self._types

    @types.setter
    def types(self, typedDict: dict) -> None:
        self._types = typedDict

    @property
    def vars(self) -> dict:
        return self._vars2pos

    @vars.setter
    def vars(self, varDict: dict) -> None:
        self._vars2pos = varDict
