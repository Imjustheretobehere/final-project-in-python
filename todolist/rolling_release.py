#NEXT = implement json, maybe dumb bozo
#NEXT = continue working on -sm, like adding the function to leave and the loop to keep you in special mode.


						#DISCLAIMER:


r"""
Experimental copy.
"""



#  the most importantest of important notes

"""
use:

randBuilder = assignRandom(stringList)

to randomize randBuilder into a 4 bit string
"""

#  Import

import json   #Mu says you're unused. (please stay unused)
import random   #gambling effects
import os   #i can see the errors already
import platform   #i can already see all the errors
import time   #the only thing i use is time.sleep()
import sys
import subprocess
import rich
from rich.console import Console
console = Console()
from rich.rule import Rule

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

#\\\\\\\\\\\\\\\\\

def specialMode():
	global todoDict, iForgotHowToEnumerate, userUser, assignRandom, stringList, dictAdd, newTask, randBuilder
	while True:
		if platform.system() == "Windows":
			os.system("cls")
		else:
			os.system("clear")
		for a, b in todoDict.items():

			print(f"-{iForgotHowToEnumerate}. (key={a}) {b}")
			iForgotHowToEnumerate += 1
		iForgotHowToEnumerate = 1

		userUser = input("-Type the key you want to delete. \n-or say the task you want to add. \n-Say -sm to exit. : ")
		if userUser == "-sm":
			return
		try:
			del todoDict[userUser]
		except KeyError:
			randBuilder = assignRandom(stringList)
			newTask = userUser
			dictAdd(randBuilder, newTask)
			print(f"-Logged {userUser} with id {randBuilder}")
			time.sleep(3)

#  Main
if platform.system() == "Windows":
	os.system("cls")
else:
	os.system("clear")


while True:
	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")

	rich.print(r"[italic]\Todo list\\[/italic]")
	print("-Welcome to the TODO LIST application")
	console.print(Rule())

	#\\Todo list\\
	#-Welcome to the TODO LIST application

	print("-Would you like to list tasks (\"-l\"), add tasks (\"-a\"), delete tasks (\"-d\"), or turn on special mode? (\"-sm\")") #literally - lol

	userUser = input() #Get input

	#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

	if (userUser == "-l"):

		if platform.system() == "Windows":
			os.system("cls")
		else:
			os.system("clear")

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

		timetosleep = len(todoDict) + 5

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
			rich.print("[red][bold]-Key does not exist. Error: KeyError[/bold][/red]")
			time.sleep(3)


		if platform.system() == "Windows":
			os.system("cls")
		else:
			os.system("clear")

	elif (userUser == "-sm"):
		specialMode()
