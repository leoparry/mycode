

import random
import time

print ("welcome to leo's fortune teller!")

name = input("what is your name\n")
print('hello', name)
color = input("what is your favourite colour?\n")
lol = input("on a scale of one to ten, how awesome are you?\n")
people = input("how many members are there of your family?\n")
place = input("Where do you live?\n")
print ("I will now select your fortune on your selection of", color, name, lol, people, place)

time.sleep(5)

fortunes = ["You will win the lottery",
            "You wil have a good life",
            "Good things will happen if you learn to code",
            "You will win some GGD glasses"]
print(random.choice(fortunes))

