#Guess the Number
from random import randint

guesses=0

rando_cunningham = randint(0,100)
while guesses < 100:
    user_response=int(input("Guess a number: "))
    guesses=guesses+1
    if user_response == rando_cunningham:
        print("Good for you! That only took " + str(guesses) + " tries.")
        break
    if user_response < rando_cunningham:
        print("Go higher.")
    if user_response > rando_cunningham:
        print("Go lower.")
