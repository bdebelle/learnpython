from sys import exit
from time import sleep
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
	print "Would you like to:"
	print "A. Taunt Bear"
	print "B. Take Honey"
	bear_moved = False

	while True:
		next = raw_input("> ")

		if next == "take honey" or next == "b":
			dead("The bear looks at you and slaps your face off.")
		elif next == "taunt bear" or next == "a" and not bear_moved:
			print "The bear has moved from the door. You can go through it now"
			print "What do you want to do now?"
			print "A. Taunt Bear"
			print "B. Take Honey"
			print "C. Open Door"
			bear_moved = True
		elif next == "taunt bear" or next == "a" and bear_moved:
			dead("The bear gets pissed and chews off your leg.")
		elif next == "open door" or next == "c" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def matrix():
	print "You are met by a man who intorduced himself as 'Morpheus'..."
	sleep(2)
	print "This is your last chance..."
	sleep(2)
	print "After this, there is no turning back..."
	sleep(2)
	print "You take the blue pill..."
	sleep(3)
 	print "-- the story ends, you wake up in your bed \nand believe whatever you want to believe.\n"
	sleep(4)
	print "You take the red pill..."
	sleep(3)
	print "-- you stay in Wonderland and I show you \nrehow deep the rabbit hole goes.\n"
	sleep(4)
	next = raw_input("blue or red?> ")

	if "blue" in next:
		dead("You wake up in your bed, feeling as if youve had the strangest dream.")
	elif "red" in next:
		dead("Welcome to the Nebuchadnezzar, Neo.")
	else:
		print "Wrong answer..."
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
	print "Want to play again?"
	print "Y or N"

	cont = raw_input(">")
	if cont == "y":
		print "Very Well..Good luck"
		sleep(3)
		start()
	else:
		print "GAME OVER"
		exit(0)

def start():
	print "You are in a dark room."
	print "There are three doors to choose from"
	print "Which do you take?"
	print "1, 2, or 3"

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






