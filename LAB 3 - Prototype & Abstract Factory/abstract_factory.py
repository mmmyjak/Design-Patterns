from abc import ABC, abstractmethod

class Shop(ABC):
    @abstractmethod
    def create_shoes(self):
        pass
    @abstractmethod
    def create_tshirt(self):
        pass

class Adidas(Shop):
    def create_shoes(self):
        return AdidasShoes()
    def create_tshirt(self):
        return AdidasTShirt()

class Nike(Shop):
    def create_shoes(self):
        return NikeShoes()
    def create_tshirt(self):
        return NikeTShirt()

class Shoes(ABC):
    @abstractmethod
    def description(self):
        pass

class TShirt(ABC):
    @abstractmethod
    def description(self):
        pass

class NikeShoes(Shoes):
    def description(self):
        return "Nike shoes"
class AdidasShoes(Shoes):
    def description(self):
        return "Adidas shoes"
class NikeTShirt(TShirt):
    def description(self):
        return "Nike t-shirt"
class AdidasTShirt(TShirt):
    def description(self):
        return "Adidas t-shirt"

def client_code(factory: Shop):
    shoes = factory.create_shoes()
    tshirt = factory.create_tshirt()

    print(shoes.description())
    print(tshirt.description())

if __name__ == "__main__":
    print("Adidas:")
    client_code(Adidas())
    print("Nike:")
    client_code(Nike())