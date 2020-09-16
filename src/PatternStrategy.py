class Strategy(object):
    def execute(self, a, b):
        raise NotImplementedError('execute')


class Solver(object):
    def __init__(self, strategy: Strategy):
        self.strategy = strategy


class ConcreteStrategyA(Strategy):
    def execute(self, a, b):
        return a+b


class ConcreteStrategyB(Strategy):
    def execute(self, a, b):
        return a-b


if __name__ == "__main__":
    solver = Solver(ConcreteStrategyA())
    solver1 = Solver(ConcreteStrategyB())
    print(solver.strategy.execute(3, 4))
    print(solver1.strategy.execute(3, 4))