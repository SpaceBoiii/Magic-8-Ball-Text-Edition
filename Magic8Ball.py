import replit
from functions import typewriter
from random import randint
from time import sleep

question = None
name = None

typewriter("Welcome! I am Cosmic, a time seer.")
sleep(1)
replit.clear()
typewriter("What's your name?")
replit.clear()
name = input("What's your name?")
if name is None:
  print("Hey, you didn't write anything... You don't deserve seeing the future.")
  quit()


typewriter("Ok, " + name.capitalize() + ", What do you want to ask me?")
replit.clear()
question = input("Alright, " + name.capitalize() + ", What did you want to ask me?")
if question is None:
  print("Hey, you didn't write anything... You don't deserve seeing the future.")
  quit()

answer = randint(1,7)
""" #Python 3.10 Solution. Doesnt work on Repl.it
match answer:
  case 1:
    typewriter("It is certain.")
  case 2:
    typewriter("Don't count on it!")
  case 3:
    typewriter("Without a doubt!")
  case 4:
    typewriter("Not likely.")
  case 5:
    typewriter("My sources say no.")
  case 6:
    typewriter("Your outlook is not so good.")
  case 7:
    typewriter("Signs point to yes!")
"""
# Python below 3.10
if answer == 1:
  typewriter("It is certain.")
  response = "It is certain."
elif answer == 2:
  typewriter("Don't count on it!")
  response = "Don't count on it!"
elif answer == 3:
  typewriter("Without a doubt!")
  response = "Without a doubt!"
elif answer == 4:
  typewriter("Not likely.")
  response = "Not likely."
elif answer == 5:
  typewriter("My sources say no.")
  response = "My sources say no."
elif answer == 6:
  typewriter("Your outlook is not so good.")
  response = "Youe outlook is not so good."
elif answer == 7:
  typewriter("Signs point to yes!")
  response = "Signs point to yes!"
else:
  print("ERROR: Generated Incorrectly")


sleep(1)
replit.clear()
print("--- CONVERSATION LOG ---")
print("8BALL: Ah Hello there.")
print("8BALL: What's your name?")
print("USER: " + name)
print("8BALL: Alright, " + name.capitalize() + ", What did you want to ask me?")
print("USER: " + question)
print("8BALL: " + response)