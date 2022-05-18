from abc import ABC, abstractmethod

class Robots(ABC):
    
    def template_method(self):
        self.go_straight()
        self.turn_left()
        self.go_straight()
        self.beep()
        self.mop()
        self.lights()

    
    def turn_left(self):
        print("Turning left")

    def beep(self):
        print("beeeeeeeeeeeeeeeeep")

    @abstractmethod
    def go_straight(self):
            pass
    
    def mop(self):
        pass

    def lights(self):
        pass


class Robot1(Robots):

    def go_straight(self):
        print("Going straight to the wall")

class Robot2(Robots):

    def go_straight(self):
        print("Going straight for 1 m")
    
    def mop(self):
        print("Cleaning with a mop")

    def lights(self):
        print("liiiights")

if __name__ == "__main__":

    print("Robot 1: ")
    r1 = Robot1()
    r1.template_method()
    print("Robot 2: ")
    r2 = Robot2()
    r2.template_method()