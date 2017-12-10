from random import randint
import time

class Die():
    def __init__(self,sides):
        self.sides = 6

    def roll_die(self):
        self.number = randint(1,self.sides)
        return self.number

newRandom = Die(6)


for i in range(0,5):
    result = newRandom.roll_die()
    print(result)

time.sleep(5)

for i in range(0,20):
    result = newRandom.roll_die()
    print(result)