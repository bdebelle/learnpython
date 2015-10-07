from sys import exit
# Allows program to abort and the number inside exit() will indicate and error or not
# 0 is a good exit, exit(100) will give different errors than exit(1) or 
# exit(2)

def gold_room():
	print "This room is full of gold. How much do you take?"

	how_much = int(raw_input("> ")) # This will allow the use of any intiger, not just 1 or 0
	if how_much >= 50:
		dead("You greedy bastard!")
	elif how_much <= 51:
		print "Nice, you're not greedy. You win!"
		exit(0) # this is an example of a good exit, No error will occur
	else:
		dead("Man, Learn to type a number.")

def bear_room():
	print "There is a bear in here!"
	print "The bear has a bnunch of honey."
	print "The fat bear is in front of another door"
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input("> ")

		if next == "take honey":
			dead("The bear looks at you and slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now"
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed and chews off your leg.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def matrix():
	print "You are met by a man who intorduced himself as 'Morpheus'..."
	print """ 
This is your last chance.
After this, there is no turning back.\n
You take the blue pill
-- the story ends, you wake up in your bed and believe whatever you want to believe.\n
You take the red pill
-- you stay in Wonderland and I show you how deep the rabbit hole goes.\n
		"""
	next = raw_input("blue or red?> ")

	if "blue" in next:
		print "You wake up in your bed, feeling as if youve had the strangest dream."
	if "red" in next:
		print "Welcome to the Nebuchadnezzar, Neo."
	else:
		bear_room()

def cthulu_room():
	print "Here you see the great evil Cthulu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head."

	next = raw_input("> ")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulu_room()

#the function dead is called in numerous spots, it will print the contents
# and explain why the user died. and then make a good exit to finish.
def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There are three doors to choose from"
	print "Which do you take?"

	next = raw_input("> ")

	if next == "1":
		bear_room()
	elif next == "2":
		cthulu_room()
	elif next == "3":
		matrix()
	else:
		dead("You stumble around the room until you starve.")





start() # calls function 'start' to begin the script










