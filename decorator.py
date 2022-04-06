import time
import random

class Component():
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        stop = random.randint(2, 10)
        print(f"Program will sleep for {stop} seconds")
        time.sleep(stop)
        

class Decorator(Component):

    def __init__(self, component: Component):
        self._component = component

    def operation(self):
        return self._component.operation()

class PrintingDecorator(Decorator):
    def operation(self):
        start = time.time()
        print(f"Start time: {time.time() - start}")
        super().operation()
        print(f"End time: {time.time() - start}")

class PrintingDecoratorExtra(Decorator):
    def operation(self):
        start = time.time()
        print(f"Start time: <<<<<{time.time() - start}>>>>>")
        super().operation()
        print(f"End time: <<<<<{time.time() - start}>>>>>")

if __name__ == "__main__":
    simple = ConcreteComponent()
    concrete1 = PrintingDecorator(simple)
    concrete2 = PrintingDecoratorExtra(concrete1)
    concrete2.operation()