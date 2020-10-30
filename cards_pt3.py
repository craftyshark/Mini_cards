#Program to read a random question or phrase from a file
#and print the game card with the user's response

import random

#open the cards against text file
f = open('cards.txt', 'r')

#read the while file and store each line in a list
cardText = f.readlines() 

#choose a random line from the list
card = random.choice(cardText)

#card chosen 
print(card)

#ask user to input noun
noun = input("Enter a noun: ")

#replace the blank with the user's input
card = card.replace("blank", noun)

#print out the game card including users respinse .
print(card)