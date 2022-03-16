from abc import ABC, abstractmethod

class Sklep(ABC):
    @abstractmethod
    def factory_method(self):
        pass
    def platnosc(self):
        product = self.factory_method()
        result = "" + product.operation()
        return result

class PłatnośćBlikiem(Sklep):
    def factory_method(self):
        return Blik()

class PłatnośćPaypalem(Sklep):
    def factory_method(self):
        return Paypal()

class Płatność(ABC):
    @abstractmethod
    def operation(self):
        pass

class Blik(Płatność):
    def operation(self):
        return "Płacisz Blikiem"
class Paypal(Płatność):
    def operation(self):
        return "Płacisz Paypalem"

a = PłatnośćBlikiem()
print(a.platnosc())