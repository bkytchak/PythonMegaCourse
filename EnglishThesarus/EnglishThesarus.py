#Author: Brent Kytchak
#Date: 9/14/2020
#Project: Creating a thesarus using python

import json

data = json.load(open("data.json"))

def translate(word):
    return data[word]

word = input("Enter word: ")

print(translate(word))
