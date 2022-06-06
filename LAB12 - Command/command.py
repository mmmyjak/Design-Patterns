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
        print(f"The player [HP:{self.health}, Level:{self.level}] attacks the enemy")
        print("...")
        if self.health > self.level:
            self.health -= self.level
            self.level +=1
            print(f"The player [HP:{self.health}, Level:{self.level}] defeated the enemy")
            return [self.health, self.level]
        else:
            exit(f"The player lost, game over with level {self.level}")

class EatCommand(Command):

    def __init__(self, health):
        self.health = health

    def execute(self):
        print("The player eats an apple")
        self.health +=5
        print(f"Your HP: {self.health}")
        return self.health

class MoveCommand(Command):

    def __init__(self, position):
        self.position = position

    def execute(self):
        random = randint(1,2)
        self.position += random
        print(f"The player moved forward by {random}, new position: {self.position}")
        return self.position

class Invoker():
    
    def __init__(self):
        self.position = 1
        self.health = 10
        self.level = 1
        self.appleCount = 0

    def game(self):
        print("The game has just started!")
        print("w = move, a = attack, c = eat apple")

        while True:
            if self.position % 5 == 0:
                print("You found an apple!")
                self.appleCount += 1

            if self.position % 3 == 0:
                print("There is an enemy in front of you! What do you want to do?")
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
                    self.position +=1
                else:
                    print("YOU CAN'T DO THIS")
            else:
                print("What do you want to do?")
                click = input()
                if click == "w":
                    self.position = MoveCommand(self.position).execute()
                elif click == "c" and self.appleCount > 0:
                    self.health = EatCommand(self.health).execute()
                    self.appleCount -= 1
                    self.position +=1
                else:
                    print("YOU CAN'T DO THIS")
                
if __name__ == "__main__":

    invoker = Invoker()
    invoker.game()