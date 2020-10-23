from utils.parser import Parser
from utils.config import ConfigFile
import yaml

def test_config(caplog):
    with open('examples/problem.yaml', 'r') as stream:
        config = yaml.safe_load(stream)
    cf = ConfigFile(config).problem
    assert type(cf.types).__name__ == 'list'
    assert len(cf.types) == 2

def test_parser_1(caplog):
    p = Parser('examples/problem.yaml', 'examples/instance.yaml')
    assert p.rawProblem.name == "labirinth"
    assert p.rawInstance.size == 2

    assert len(p.problem.types) == 2

    p.problem.setTypes(p.rawProblem.types)
    assert "position" in p.problem.types

    instantiated_variables = p.problem.instantiateVar(p.rawProblem.variables, 
                                                      p.rawInstance.variables)
    assert "treasure_0" in instantiated_variables
    assert "treasure_1" in instantiated_variables
    assert len(instantiated_variables) == 8
    # p.problem.generateState(p.rawProblem.variables, p.rawInstance.variables)
