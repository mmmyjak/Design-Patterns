from abc import ABC, abstractmethod

class Context():
    
    def __init__(self, strategy, kwota):
        self._strategy = strategy
        self.kwota = kwota
    
    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def rozliczenie(self):
        return f"Kwota podatku do zapłaty: {self._strategy.sposob(self.kwota)}"

class Strategy(ABC):

    @abstractmethod
    def sposob(self, kwota):
        pass

class MlodaStrategia(Strategy):

    def sposob(self, kwota):
        if kwota > 85000:
            return 0.19*kwota
        else:
            return 0

class ZwyklaStrategia(Strategy):

    def sposob(self, kwota):
        if kwota > 85000:
            return 0.32*kwota
        else:
            return 0.19*kwota

class Dywidenda(Strategy):

    def sposob(self, kwota):
        return 0.04*kwota

if __name__ == "__main__":

    wiek = int(input("Podaj wiek: "))
    zarobki = float(input("Podaj zarobki: "))

    if input("Czy chodzi o dywidendę z USA (KLIKNIJ ENTER, JEŚLI NIE): "):
        print(Context(Dywidenda(), zarobki).rozliczenie())
    else:
        if wiek < 26:
            print(Context(MlodaStrategia(), zarobki).rozliczenie())
        else:
            print(Context(ZwyklaStrategia(), zarobki).rozliczenie())
