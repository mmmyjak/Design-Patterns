from abc import ABC, abstractmethod

class Originator():

    def __init__(self):
        self._state = None
    
    def dosmth(self, text):
        print(f"State: {text}")
        self._state = text
    
    def save(self):
        memento =  ConcreteMemento(self._state)
        print(f"Saved {memento.get_text()}")
        return memento

    def restore(self, memento):
        self._state = memento.get_text()


class Memento(ABC):
    @abstractmethod
    def get_text(self):
        pass

class ConcreteMemento(Memento):
    def __init__(self, state):
        self._state = state
    
    def get_text(self):
        return self._state

class Caretaker():

    def __init__(self, originator):
        self._mementos = []
        self._originator = originator

    def backup(self):
        self._mementos.append(self._originator.save())

    def undo(self):
        if not len(self._mementos):
            print("There are no snapshots")
            return      
        memento = self._mementos.pop()
        print(f"Restoring state to {memento.get_text()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()
    
        

if __name__ == "__main__":
    originator = Originator()
    caretaker = Caretaker(originator)
    while True:
        inp = input()
        if inp == "> Snapshot":
            caretaker.backup()
        elif inp == "> Undo":
            caretaker.undo()
        elif inp == "> Exit":
            break
        else:
            originator.dosmth(inp)

