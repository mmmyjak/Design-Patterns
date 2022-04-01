from __future__ import annotations
from abc import ABC, abstractmethod

class Component(ABC):
    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component):
        pass

    def remove(self, component: Component):
        pass

    def is_composite(self) -> bool:
        return False
    
    @abstractmethod
    def prize(self) -> int:
        pass

class Product(Component):
    def __init__(self, pprize):
        self.prod_prize = pprize
    def prize(self) -> int:
        return self.prod_prize

class Box(Component):
    def __init__(self):
        self.children = []
    
    def add(self, component: Component):
        self.children.append(component)
        component.parent = self
    
    def remove(self, component: Component):
        self.children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def prize(self) -> int:
        result = 0
        for child in self.children:
            result += child.prize()
        return result


if __name__ == "__main__":
    ball = Product(50)
    main_ = Box()
    box1 = Box()
    box2 = Box()
    box2.add(ball)
    box2.add(Product(30))
    tinybox = Box()
    tinybox.add(Product(2.50))
    box2.add(tinybox)
    box1.add(Product(300))
    box1.add(Product(45))
    main_.add(box1)
    main_.add(box2)
    print(tinybox.children)
    print(main_.prize())