from abc import ABC, abstractmethod

from numpy import product

class Builder(ABC):
    @property
    @abstractmethod
    def product(self):
        pass
    @abstractmethod
    def add_cheese(self):
        pass
    @abstractmethod
    def add_pepperoni(self):
        pass
    @abstractmethod
    def add_ham(self):
        pass
    @abstractmethod
    def add_mushrooms(self):
        pass

class Pizza():
    def __init__(self):
        self.parts = []
    def add(self, ingredient):
        self.parts.append(ingredient);
    def all_ingredients(self):
         print(f"Ingredients: {', '.join(self.parts)}")

class ConcreteBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Pizza()
    
    @property
    def product(self):
        return self._product

    def add_cheese(self):
        self._product.add("Cheese")

    def add_pepperoni(self):
        self._product.add("Pepperoni")
        
    def add_ham(self):
        self._product.add("Ham")

    def add_mushrooms(self):
       self._product.add("Mushrooms")

class Director():
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def build_margherita(self):
        self.builder.add_cheese()
    
    def build_pepperoni(self):
        self.builder.add_cheese()
        self.builder.add_pepperoni()

    def build_capricciosa(self):
        self.builder.add_cheese()
        self.builder.add_ham()
        self.builder.add_mushrooms()


director = Director()
builder = ConcreteBuilder()
director.builder = builder
print("Margherita")
director.build_margherita()
builder.product.all_ingredients()
builder.reset()

print("Pepperoni")
director.build_pepperoni()
builder.product.all_ingredients()
builder.reset()

print("Capricciosa")
director.build_capricciosa()
builder.product.all_ingredients()






