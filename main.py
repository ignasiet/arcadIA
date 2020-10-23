from utils.parser import Parser


def load_and_verify(problem: str, instances: str):
    p = Parser(problem, instances)
    print(p.problem)


if __name__ == "__main__":  # pragma: no cover
    load_and_verify('examples/problem.yaml', 'examples/instance.yaml')
