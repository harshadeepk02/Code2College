#Harshadeep K. | Elite101 PreWork | Chatbot

import random

def greetings(name):
  response = random.randint(1,4)
  if len(name) > 10:
    print("Wow, " + name + ", that's quite the long name!")
  elif response == 1:
    print("Greetings, " + name + "!")
  elif response == 2:
    print("Hello, " + name + "!")
  elif response == 3:
    print("Hi there, " + name + "!")
  elif response == 4:
    print(name + ", huh? That's a pretty cool name!")
  print("Nice to meet you!" + "\n")


def weather():
  weather = input("How's the weather today? ")
  good_weather = ["sunny", "clear", "fair", "fine", "good"]
  bad_weather = ["rainy", "cloudy", "windy", "stormy", "bad"]
  weather1 = random.choice(good_weather)
  weather2 = random.choice(bad_weather)
  if weather in good_weather:
    print("That's great to hear!")
    print("The weather here is " + weather1 + "." + "\n")
  elif weather in bad_weather:
    print("That's unfortunate, hopefully it clears up soon.")
    print("The weather here is " + weather2 + ", so it's not the greatest for me either..." + "\n")
  else:
    myweather = random.choice(good_weather)
    print("Cool, the weather here is " + myweather + "." + "\n")


def smalltalk():
  response = random.randint(1,2)
  
  if response == 1:
    answer = input("Did you do anything interesting today? ")
    if "no" in answer:
      print("Ah, just an average boring day then? Me too..." + "\n")
    else:
      print("Huh, that sounds like it was fun!" + "\n")
      
  if response == 2:
    option = random.randint(1,3)
    answer = input("Have you seen any cool movies recently? ")
    if "no" in answer:
      print("Yeah, I haven't been watching many movies nowadays either.")
    elif option == 1:
      print("Oh, I've heard of that one! I still haven't watched it yet though, I should probably check it out sometime.")
    elif option == 2:
      print("I remember watching that one, it was pretty good!")
    elif option == 3:
      print("Never heard of that movie, maybe I should check it out...")
    print("\n")


def joke():
  answer = input("Oh! Wanna hear a joke I just remembered? ")
  if "no" in answer:
    print("Too bad, you get to hear it anyways!")
  joke = random.randint(1,5)
  if joke == 1:
    wait = input("What do you call a fake noodle? ")
    print("An im-pasta!")
  elif joke == 2:
    wait = input("What did the left eye say to the right eye? ")
    print("Between us, something smells!")
  elif joke == 3:
    wait = input("Why did the student eat his homework? ")
    print("Because the teacher said it was a piece of cake!")
  elif joke == 4:
    wait = input("What kind of lion can't roar? ")
    print("A dandelion!")
  elif joke == 5:
    wait = input("What animal is at every baseball game? ")
    print("A bat!")
  print("Okay, that was pretty bad but at least I tried?")
  print("\n")

def generic():
  repeat = True
  wait = input("Anything else you wanna talk about? ")
  while repeat == True:
    rand = random.randint(1,4)
    if "no" in wait:
      print("Okay, thanks for chatting!")
      break
    elif rand == 1:
      print("That's cool!")
    elif rand == 2:
      print("Wow!")
    elif rand == 3:
      print("Oh really?")
    elif rand == 4:
      print("Interesting...")
    wait = input("Tell me more! ")
    print("\n")
    
    
  
  
  




print("Hello, I am ChatBot, an interactive program that can talk and interact with users!")
name = input("What is your name?: ")
greetings(name)
weather()
smalltalk()
joke()
generic()
