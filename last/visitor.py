from abc import ABC, abstractmethod

class Component(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass

class StringComponent(Component):

    def __init__(self, string):
        self.string = string

    def accept(self, visitor):
        visitor.visit_string(self)

    def reversed_string(self):
        print(self.string[::-1])

    def normal_string(self):
        print(self.string)

class DictionaryComponent(Component):

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def accept(self, visitor):
        visitor.visit_dictionary(self)

    def niceDictionary(self):
        for key in self.dictionary:
            print(key, '->', self.dictionary[key])

class Visitor(ABC):

    @abstractmethod
    def visit_string(self, component):
        pass

    @abstractmethod
    def visit_dictionary(self, component):
        pass

class Visitor1(Visitor):

    def visit_string(self, component):
        component.reversed_string()

    def visit_dictionary(self, component):
        print()

class Visitor2(Visitor):

    def visit_string(self, component):
        component.normal_string()

    def visit_dictionary(self, component):
        component.niceDictionary()

def client_code(components, visitor):
    
    for component in components:
        component.accept(visitor)

if __name__ == "__main__":

    components = [StringComponent("Jakiś string"), DictionaryComponent({'foo': 'bar'})]

    print("Visitor 1")
    visitor1 = Visitor1()
    client_code(components, visitor1)

    print("Visitor 2")
    visitor2 = Visitor2()
    client_code(components, visitor2)