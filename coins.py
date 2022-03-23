import random

#while true
print("welcome to coin game")
print("The first coin will always be heads")
print("The chance of both coins being heads is 50%")
print()


tails = 0
heads = 1

coin0 = 1

if float(coin0) < 0.5: coinstatus0 = "tails"
else: coinstatus0 = "heads"

print("The first coin is " + coinstatus0)

#the second coin

coin1 = random.random()

if float(coin1) < 0.5: coinstatus1 = "tails"
else: coinstatus1 = "heads"

print("The second coin is " + coinstatus1)

if coinstatus0 == "heads" and coinstatus1 == "heads":
    print()
    print("WINNER")