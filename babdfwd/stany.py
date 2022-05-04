from abc import ABC, abstractmethod
from time import sleep
from random import randint
import datetime

def oczekiwanie():
    _random = randint(1,5)
    for i in range(_random):
        sleep(1)
        print("...")

class Context:

    _state = None

    def __init__(self, state):
        self.transition_to(state)

    def transition_to(self, state):
        self._state = state
        self._state.context = self
        self.action()


    def action(self):
        _bool = self._state.inform()
        if _bool:
            self._state.handle2()
        else:
            self._state.handle1()

        
class State(ABC):

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @abstractmethod
    def handle1(self):
        pass

    @abstractmethod
    def handle2(self):
        pass

    @abstractmethod
    def inform(self):
        pass


class Automat(State):

    def inform(self):
        print("Rozmowa z automatem")
        oczekiwanie()
        answer = input("Czy problem został rozwiązany? [TAK/NIE]")
        if answer.upper() == "TAK":
            return True
        else:
            return False

    def handle1(self):
        print("Przechodzisz do kolejki")
        self.context.transition_to(Kolejka())
    
    def handle2(self):
        print("Cieszymy się, że mogliśmy pomóc")


class Kolejka(State):
    def inform(self):
        print("Czekasz w kolejce na 1 linię wsparcia")
        oczekiwanie()
        if datetime.datetime.now().hour < 8:
            return True
        else:
            return False

    def handle1(self):
        print("Łączysz się z pierwszą linią wsparcia")
        self.context.transition_to(PierwszaLiniaWsparcia())
    
    def handle2(self):
        print("Niestety linia wsparcia aktualnie nie funkcjonuje")

class PierwszaLiniaWsparcia(State):
    def inform(self):
        print("Rozmowa z pierwszą linią wsparcia")
        oczekiwanie()
        answer = input("Czy problem został rozwiązany? [TAK/NIE]")
        if answer.upper() == "TAK":
            return True
        else:
            return False

    def handle1(self):
        print("Nie możemy Ci pomóc, przekierujemy Cię do drugiej linii wsparcia")
        self.context.transition_to(DrugaLiniaWsparcia())
    
    def handle2(self):
        print("Cieszymy się, że mogliśmy pomóc")

class DrugaLiniaWsparcia(State):
    def inform(self):
        print("Rozmowa z drugą linią wsparcia")
        oczekiwanie()
        answer = input("Czy problem został rozwiązany? [TAK/NIE]")
        if answer.upper() == "TAK":
            return True
        else:
            return False

    def handle1(self):
        print("Przykro nam, że nie mogliśmy pomóc")
    
    def handle2(self):
        print("Cieszymy się, że mogliśmy pomóc")

if __name__ == "__main__":
    context = Context(Automat())