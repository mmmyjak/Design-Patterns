from abc import ABC, abstractmethod

class Subject(ABC):

    @abstractmethod
    def attach(self, observer):
        pass
    @abstractmethod
    def detach(self, observer):
        pass
    @abstractmethod
    def notify(self):
        pass

class ConcreteSubject(Subject):
    _observers = []
    _strategy = None
   
    @property
    def strategy(self):
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def update_room(self):
        _rooms = {"1": KitchenStategy, "2": BedroomStrategy, "3": BathroomStrategy}
        _input = input("Where are you?\n")

        if _input in _rooms:
            self._strategy = _rooms[_input]
            self.notify()
        else:
            print("Nie ma takiego pokoju")

class Observer(ABC):

    @abstractmethod
    def update(self, subject):
        pass

class BulbObserver(Observer):
    def update(self, subject):
        subject._strategy().bulb()

class KettleObserver(Observer):
    def update(self, subject):
        subject._strategy().kettle()

class AirConditioningObserver(Observer):
    def update(self, subject):
        subject._strategy().airc()

class Strategy(ABC):
    @abstractmethod
    def bulb(self):
        pass    
    @abstractmethod
    def kettle(self):
        pass
    @abstractmethod
    def airc(self):
        pass

class KitchenStategy(Strategy):
    def bulb(self):
        print("Włączam żarówkę w kuchni")
    def kettle(self):
        print("Gotuję wodę")
    def airc(self):
        print("Ustawiam temperaturę na 20 stopni")


class BedroomStrategy(Strategy):
    def bulb(self):
        print("Włączam żarówkę w sypialni")
    def kettle(self):
        print()
    def airc(self):
        print("Ustawiam temperaturę na 22 stopnie")


class BathroomStrategy(Strategy):
    def bulb(self):
        print("Włączam żarówkę w łazience")
    def kettle(self):
        print()
    def airc(self):
        print("Ustawiam temperaturę na 18 stopni")

if __name__ == "__main__":
    subject = ConcreteSubject()
    subject.attach(BulbObserver())
    subject.attach(KettleObserver())
    subject.attach(AirConditioningObserver())
    subject.update_room()