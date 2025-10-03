"""This is simple dice project that takes sides from the user and prints the random number"""
from random import randint

class Dice:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

die_one = Dice()
die_one.roll_die()
die_two = Dice(10)
die_two.roll_die()