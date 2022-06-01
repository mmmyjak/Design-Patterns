from abc import ABC, abstractclassmethod
from sys import exit
from random import randint

class Command(ABC):

    @abstractclassmethod
    def execute():
        pass

class AttackCommand(Command):

    def __init__(self, health, level):
        self.health = health
        self.level = level
    
    def execute(self):
        print(f"Gracz [HP:{self.health}, Level:{self.level}] atakuje wroga")
        print("...")
        if self.health > self.level:
            self.health -= self.level
            self.level +=1
            print(f"Gracz [HP:{self.health}, Level:{self.level}] pokonał wroga")
            return [self.health, self.level]
        else:
            exit(f"Gracz przegrał, koniec gry z poziomem {self.level}")

class EatCommand(Command):

    def __init__(self, health):
        self.health = health

    def execute(self):
        print("Gracz je jabłko")
        self.health +=5
        print(f"Życie wynosi teraz: {self.health}")
        return self.health

class MoveCommand(Command):

    def __init__(self, position):
        self.position = position

    def execute(self):
        random = randint(1,2)
        self.position += random
        print(f"Gracz poszedł do przodu o {random} pozycje, jego pozycja teraz to: {self.position}")
        return self.position

class Invoker():
    
    def __init__(self):
        self.position = 1
        self.health = 10
        self.level = 1
        self.appleCount = 0

    def game(self):
        print("Gra się zaczęła")
        print("w = move, a = attack, c = eat apple")

        while True:
            if self.position % 5 == 0:
                print("Znalazłeś jabłko")
                self.appleCount += 1

            if self.position % 3 == 0:
                print("Przed tobą stoi przeciwnik. Co chcesz zrobić?")
                click = input()
                if click == "w":
                    self.position = MoveCommand(self.position).execute()
                elif click == "a":
                    comm = AttackCommand(self.health, self.level).execute()
                    self.health = comm[0]
                    self.level = comm[1]
                    self.position +=1
                elif click == "c" and self.appleCount > 0:
                    self.health = EatCommand(self.health).execute()
                    self.appleCount -= 1
                else:
                    print("Nie możesz tego zrobić")
            else:
                print("Co chcesz zrobić?")
                click = input()
                if click == "w":
                    self.position = MoveCommand(self.position).execute()
                elif click == "c" and self.appleCount > 0:
                    self.health = EatCommand(self.health).execute()
                    self.appleCount -= 1
                else:
                    print("Nie możesz tego zrobić")
                
if __name__ == "__main__":

    invoker = Invoker()
    invoker.game()
