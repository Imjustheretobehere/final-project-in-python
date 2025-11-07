						#DISCLAIMER:


r"""
 ___    ____ ___  _   _ _     ____  _   _ _ _____ 
|_ _|  / ___/ _ \| | | | |   |  _ \| \ | ( )_   _|
 | |  | |  | | | | | | | |   | | | |  \| |/  | |  
 | |  | |__| |_| | |_| | |___| |_| | |\  |   | |  
|___|_ \____\___/_\___/|_____|____/|_| \_|   |_|  
|  ___|_ _| \ | |_ _/ ___|| | | |                 
| |_   | ||  \| || |\___ \| |_| |                 
|  _|  | || |\  || | ___) |  _  |                 
|_|   |___|_| \_|___|____/|_| |_|                  
																																					

Nows the time to tell you i should have implemented json, BUT I DIDNT!
I worked on this for 2 days. 2 days, pretty impressive huh? 
(please say yes im begging you to compliment me if you can't tell)

(i know you can)

Please dont delete this link. oh wait if you delete it you cant see this, huh?
so uh, if you want to criticize my work, think about this first.

i appreciate any and all feedback

"""



#  the most importantest of important notes

"""
use:

randBuilder = assignRandom(randBuilder, stringList)

to randomize randBuilder into a 4 bit string
"""

#  Import

import json   #Mu says you're unused. (please stay unused)
import random   #gambling effects
import os   #i can see the errors already
import platform   #i can already see all the errors
import time   #the only thing i use is time.sleep()

#  Define

iForgotHowToEnumerate = 1

userUser = "Lorem ipsum dolor sit amet. "

todoDict = {
	#"Placeholder": "data (used for testing purposes)"
}

randBuilder = "" #used in function assignRandom

stringList = ["a", "b", "c", "d", "e", "f", 
				"g", "h", "i", "j", "k", "l", 
				"m", "n", "o", "p", "q", "r", 
				"s", "t", "u", "v", "w", "x", 
				"y", "z", "0", "1", "2", "3", 
				"4", "5", "6", "7", "8", "9",]
				#Yeah, I forgot to add uppercase. what are you gonna do about it?

newTask = "" #used for strings for adding to dicts uh wait uh im not explaining this to you

timetosleep = len(todoDict) + 5

#OTHER SECTION HEEHEEHEEEHAWHEEEHEEEHEEEHAW

def assignRandom(stringList):
	"""Assigns a random 4-character string that doesn't exist in todoDict yet."""

	while True:
		randBuilder = ""
		for _ in range(4):
			randBuilder += random.choice(stringList)

		if randBuilder not in todoDict:
			return randBuilder
		# if it exists, loop again to generate a new one


		else:
			return randBuilder

#\\\\\\\\\\\\\\\\\

def dictAdd(randBuilder, newTask):
	""" Function to add to the dict. """
	todoDict[randBuilder] = newTask 
	print("-Maybe a success, maybe not, you will never know.") #Even i dont know 

#\\\\\\\\\\\\\\\\\

#  Main
if platform.system() == "Windows":
	os.system("cls")
else:
	os.system("clear")


while True:
	print("\033[3m\\\\Todo list\\\\\033[0m")
	print("-Welcome to the TODO LIST application")

	#\\Todo list\\
	#-Welcome to the TODO LIST application

	print("-Would you like to list tasks (\"-l\"), add tasks (\"-a\"), or delete tasks? (\"-d\")") #literally - lol

	userUser = input() #Get input

	#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

	if (userUser == "-l"):

		for a, b in todoDict.items():

			print(f"-{iForgotHowToEnumerate}. (key={a}) {b}")
			iForgotHowToEnumerate += 1
		iForgotHowToEnumerate = 1
		time.sleep(timetosleep)


		if platform.system() == "Windows":
			os.system("cls")
		else:
			os.system("clear")

	#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

	elif (userUser == "-a"):

		randBuilder = assignRandom(stringList)
		newTask	= input("-Please enter your new task : ")
		dictAdd(randBuilder, newTask)

		if platform.system() == "Windows":
			os.system("cls")
		else:
			os.system("clear")

	#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

	elif (userUser == "-d"):
		userUser = input("-Please say the key of the dict item you would like to delete : ")
		try:
			del todoDict[userUser]
		except KeyError:
			print("\033[0;31m-Key does not exist. Error: KeyError\033[0m")
			time.sleep(3)


		if platform.system() == "Windows":
			os.system("cls")
		else:
			os.system("clear")