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