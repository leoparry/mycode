

import random
import time

print ("welcome to leo's fortune teller")

name = input("what is your name\n")
color = input("what is your favourite colour?")
print ("I will now select your fortune on your selection of", color)

time.sleep(2)

fortunes = ["You will win the lottery",
            "You wil have a good life",
            "Good things will happen if you learn to code",
            "You will win some GGD glasses"]
print(random.choice(fortunes))

