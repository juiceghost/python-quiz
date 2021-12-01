#Ex1
import random

def roll():
    return random.randint(1,6)

#Ex2
total = 0

for i in range(10000):
    total += roll()

avg_roll = float(total) / 10000

print(avg_roll)