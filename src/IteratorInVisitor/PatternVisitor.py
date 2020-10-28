from abc import ABCMeta, abstractmethod
from patterns.src.IteratorInVisitor import PatternIterator as pi
from typing import List

class Visitor(metaclass=ABCMeta):

    @abstractmethod
    def visit_concrete_component_a(self, element: 'ConcreteComponentA') -> None:
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element: 'ConcreteComponentB') -> None:
        pass

class Component(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

class ConcreteComponentA(Component, pi.ListIterator):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_component_a(self)


class ConcreteComponentB(Component, pi.DictIterator):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_component_b(self)


class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        pi.chooseYourCollection(element)

    def visit_concrete_component_b(self, element: 'ConcreteComponentB') -> None:
        pass

class ConcreteVisitor2(Visitor):
    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        pi.chooseYourCollection(element)

    def visit_concrete_component_a(self, element: 'ConcreteComponentA') -> None:
        pass

def client_code(components: List[Component], visitor: Visitor):
    for component in components:
        component.accept(visitor)


if __name__ == "__main__":
    components = [ConcreteComponentA([132, 4214, 514125, 213124, 32141]), ConcreteComponentB({'Kirill': 132, 'Nastya': 4214, 'Pasha': 514125, 'Sanya': 213124, 'Anton': 32141})]
    visitor1 = ConcreteVisitor1()
    client_code(components, visitor1)

    print('------------------')

    visitor2 = ConcreteVisitor2()
    client_code(components, visitor2)