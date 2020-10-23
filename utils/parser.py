import yaml
from utils.config import ConfigFile
from utils.problem import Problem
from typing import TypeVar, List, Callable, Set, Deque, Dict, Any, Tuple, Optional
from .action import Action


class Parser():
    def __init__(self, problem, instance):
        self.rawProblem = self.loadFile(problem).problem
        self.rawInstance = self.loadFile(instance).instance
        self.problem = Problem()
        self.types = {}
        self.vars2pos = {}
        self.actions = {}
        self.parse()

    def loadFile(self, filename):
        # instantiate
        with open(filename, 'r') as stream:
            config = yaml.safe_load(stream)
        # return ConfigFile(config).problem
        return ConfigFile(config)

    def getProblem(self):
        return str(self.problem)
    
    def getInstance(self):
        return str(self.instance)

    def parse(self):
        self.problem.types = self.setTypes(self.rawProblem.types)
        self.problem.vars2pos, numberVars = self.generateVars(
                                           self.rawProblem.variables,
                                           self.rawInstance.initial)
        self.problem.initialstate = self.extractInitialState(
                                    self.rawInstance.initial,
                                    numberVars)
        self.problem.goalTest = self.extractGoalCondition(self.rawInstance.goal.conditions)
        self.problem.actions.extend(self.parseActions(self.rawProblem.actions, self.rawInstance.initial))

    def extractGoalCondition(self, conditions: dict) -> str:
        return self.extractFormula(conditions)

    def extractFormula(self, conditions: dict, replace: str=None, substitute: str=None) -> str:
        listFormulas = []
        for condition in conditions:
            listFormulas.append(condition.operator.join(
                [f"state[{self.problem.vars2pos[operand.strip()]}]"
                if operand.strip() in self.problem.vars2pos
                else f"state[{self.problem.vars2pos[operand.replace(replace, substitute).strip()]}]"
                if replace == operand.split('.')[0]
                else str(operand.strip())
                for operand in condition.operands.split(',')
                ]))
        formula = " and ".join(listFormulas)
        return formula

    def extractInitialState(self, instances: dict, number: int) -> list:
        initialState = [None] * number
        for key, value in instances:
            self.extractState(key, value, initialState)
        return initialState

    def extractState(self, key: str, value: Any, initialState: list) -> None:
        if isinstance(value, int):
            initialState[self.problem.vars2pos[key]] = value
        elif isinstance(value, dict):
            for item in value:
                initialState[self.problem.vars2pos[key+"."+item]] = value[item]
        elif isinstance(value, list):
            for item in value:
                instance = str(item['instance'])
                clDict = item.copy()
                clDict.pop('instance')
                self.extractState(key+"."+instance, clDict, initialState)

    def generateVars(self, variables: list, instances: list) -> Tuple[dict, int]:
        pos = 0
        vars2pos = {}
        instantiatedVariables = self.instantiateVar(variables, instances)
        self.complexVariables(instantiatedVariables, variables)
        for key in instantiatedVariables:
            if type(instantiatedVariables[key]).__name__ == 'list':
                for var in instantiatedVariables[key]:
                    vars2pos[var] = pos
                    pos += 1
            else:
                vars2pos[instantiatedVariables[key]] = pos
                pos += 1
        return vars2pos, pos

    def instantiateVar(self, variables: list, instances: dict) -> list:
        # 1 case: var is instantiable: instantiate then and return a list of instantiated vars
        retList = {}
        for var in variables:
            if "instantiable" in var and var.instantiable is True:
                listInstances = instances[var.name]
                for instance in listInstances:
                    if var.name in retList:
                        newValue = {var.name: [f'{var.name}.{instance["instance"]}', 
                                               retList[var.name]]}
                        retList.update(newValue)
                    else:
                        retList[var.name] = f'{var.name}.{instance["instance"]}'
            else:
                retList[var.name] = var.name
        return retList

    def complexVariables(self, instantiatedVariables: list, variables: list) -> None:
        # 2 case: var is custom type so treat it here
        for var in variables:
            if var.type in self.problem.types:
                instantiatedVar = instantiatedVariables[var.name]
                if type(instantiatedVar).__name__ == 'list':
                    attributedVars = []
                    for instance in instantiatedVar:
                        attributedVars.extend(self.setAttributes(var.type,
                                                                 instance))
                    instantiatedVariables.update({var.name: attributedVars})
                else:
                    instantiatedVariables.update({var.name: self.setAttributes(var.type,
                                                                               var.name)})

    def setAttributes(self, typed: str, var: str) -> list:
        newVars = []
        for attribute in self.problem.types[typed]:
            newVars.append(f'{var}.{attribute.name}')
        return newVars

    def setTypes(self, types: dict) -> None:
        typedDict = {}
        for t in types:
            typedDict[t.name] = t.variables
        return typedDict

    def parseActions(self, actionList: dict, initialState: dict) -> list:
        actions = []
        for action in actionList:
            if 'instantiable' in action:
                pass
                instantiated = self.instantiateAction(action, initialState[action.instantiable])
                actions.extend(instantiated)
            else:
                a = Action(action.name)
                a.preconditions = self.extractFormula(action.preconditions)
                actions.append(a)
        return actions

    def instantiateAction(self, action: dict, var: dict) -> list:
        actionsList = []
        for instance in var:
            a = Action(action.name+"_"+str(instance['instance']))
            a.preconditions = self.extractFormula(action.preconditions,
                                                  action.instantiable,
                                                  f"{action.instantiable}.{str(instance['instance'])}")
            actionsList.append(a)
        return actionsList
