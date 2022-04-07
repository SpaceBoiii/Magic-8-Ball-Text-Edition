import replit
from functions import typewriter
from random import randint
from time import sleep
import time

from random import randint as t
import cursor

cursor.hide()


def clear():
    print("\033c",end = "")


def load():
  suc = "\033[1m\033[38;2;255;0;0m"
  what = ["Cosmic is Time Traveling", "Cosmic is Learning Everything", "Cosmic is Returning", "Cosmic is Writing Your File", "Cosmic is Activating Interface"]
  lLen = ["\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m"] 
  
  for j in range(len(what)):
    for c in range(t(3, 7)):
      for i in range(len(lLen)):
        lLen[i] = suc + "\033[4m\033[38;2;255;0;255m\033[1m    \033[0m"
        print("\033[48;2;255;50;75m              \033[1mLOADING              \033[0m\n\nStatus [\033[93m" + str(j + 1) + "\033[0m - \033[93m"+ str(len(what)) + "\033[0m]\n\033[1m" + what[j]+"\033[0m\n\033[1m"+ "".join(lLen)+ "\033[0m\n\n\033[48;2;255;50;75m              \033[1mLOADING              \033[0m")

        lLen[i] = "\033[4m\033[1m \033[0m"
        time.sleep(0.065)
        print("\033c",end = "")


  clear()        
  print("\033[48;2;50;255;75m               \033[1mDONE              \033[0m\n") 
  lLen[i] = suc + "__\033[0m"
  print("Status [\033[38;2;0;255;0m" + str(j + 1) + "\033[0m - \033[38;2;0;255;0m"+ str(len(what)) + "\033[0m]")
  #print("\033[1m" + what[j]+"\033[0m") 
  #print("\033[1m"+ "".join(lLen)+ "\033[0m")
  print("\n\033[48;2;50;255;75m               \033[1mDONE              \033[0m")    
  input("\n\n\t[ENTER] >") 
  clear()       



load()

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