class Flyweight():
    
    def __init__(self, shared: str):
        self.shared = shared
    
    def operation(self, unique: str):
        print(f"Flyweight:\nShared: {self.shared}\nUnique: {unique}")

class FlyweightFactory():
    flyweights = dict()
    number = 9000
    def __init__(self, initial: dict):
        FlyweightFactory.number += 1
        for ini in initial:
            self.flyweights[FlyweightFactory.number] = Flyweight(ini)
    
    def getFlyweight(self, shared_dict):
        print(list(self.flyweights.keys()))
        key = list(self.flyweights.keys())[shared_dict]

        if not self.flyweights.get(key):
            print("Created new flyweight")
            self.flyweights[key] = Flyweight(shared_dict)

        return self.flyweights[key]

    def listFlyweights(self):
        count = len(self.flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        for fly in self.flyweights:
            print(fly)
    
def add_new_coordinate(factory: FlyweightFactory, x, y, texture, color):
    print("Client: Adding a car to database.")
    flyweight = factory.getFlyweight([texture, color])
    flyweight.operation([x, y])

if __name__ == "__main__":
    
    factory = FlyweightFactory([
        [131, "red"],
        [121, "blue"],
        [101, "green"]
    ])

    factory.listFlyweights()

    add_new_coordinate(factory, 0, 0, 131, "red")
    add_new_coordinate(factory, 8, 132, 101, "green")
    print("\n")
    factory.listFlyweights()
    