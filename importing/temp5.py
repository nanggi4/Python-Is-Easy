from random import random

randVal = random()
print(randVal)

upper = 1.0
lower = 0.0
guess = 0.5

while(True):
  if guess == randVal:
    break
  elif guess < randVal:
    