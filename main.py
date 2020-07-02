from utils.parser import Parser


def load_and_verify(problem):
    p = Parser(problem)
    print(p.problem())


if __name__ == "__main__":  # pragma: no cover
    load_and_verify("examples/problem.yaml")
