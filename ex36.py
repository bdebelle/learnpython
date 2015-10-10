# Crack the Code
from sys import exit
import time
from time import sleep
import random

prompt = ">"

	
def dungeon():
	print """

You awake in a dark dank dungeon. 
You have been captured by the enemy in a recent battle 
and now await execution. 

You barely notice the dying man to your right. 

	"Young kight, what is your name?" he asks
"""

	name = raw_input(prompt)

	print 	"very well %s, " % name 
	sleep(3)
	print """
The man hands you a dagger...
"Take this, I dont think ill live long enough to use it."
"""
	sleep(3)
	print """
With his dying breath.... 
he passes you a dagger and you tuck
it behind your back. 
"""
	sleep(3)
	print "You hear a guard making his way toward you cell"

	sleep(3)
	print """
	Guard: Prisoner... walk toward the gate. Your time has come.

	wearily, you stand and walk towards the door, clutching
	the old man's dagger behind your back. 

	the guard opens the door and enters. 
	"""
	sleep(3)
	print"""
	What do you do?

	1. Attack the Guard with the dagger
	2. Beg for mercy.

	"""
	choice = int(raw_input(prompt))
	if choice == 1:
		print "Quickly you lunge at the guard"
		critical_hit = random.randint(1, 6)
		print "Your chance of landing is critical hit is %d" % critical_hit
		if critical_hit >=3:
			print "You stick the guard in the throat. Killing him."
			print "You steal his keys and clothing. "
			print "And exit only to find yourself in a hallway."
			
			hallway()
		else: 
			dead("You are too slow and the gaurd kills you.")
	elif choice == 2:
		dead("No mercy is granted.")
	else:
		dead("You are escorted to the gallows and hung.")

def hallway():
	sleep(2)
	print "This hallway has 3 doors"
	print """
	Do you choose
	1. A large door to your left
	2. The door at the top of the stairs
	3. The small door to the right	
	"""
	choice = raw_input(prompt) 
	if choice.isdigit(): 
		door = int(choice)
	else:
		dead("Wrong answer fool.")
	
	if door == 1:
		armory()
	elif door == 2:
		throne_room()
	elif door == 3:
		courtyard()
	else:
		dead("More guards arrive and capture you.")

def armory():
	print "You find yourself in the armory"
	print "There is a large guard dog standing in front of another door."
	print """
	Do you choose
	A. Kill dog 
	B. Throw him a bone	
	"""
	dog_moved = False
	
	while True:
		next = raw_input("> ")

		if next == "Kill dog" or next == "a":
			dead("The hound tears you to shreds")
		elif next == "throw him a bone" or next == "b" and not dog_moved:
			print "The dog slinks off to enjoy the bone."
			print "What do you want to do now?"
			print "A. Kill dog"
			print "B. Throw him another bone"
			print "C. Open Door"
			print "D. Turn back"
			dog_moved = True
		elif next == "throw him a bone" or next == "b" and dog_moved:
			dead("You hit the dog with the bone and he tears you to shreds.")
		elif next == "open door" or next == "c" and dog_moved:
			courtyard()
		elif next == "turn back" or next == "d" and dog_moved:
			hallway()
		else:
			dead("A guard enters the room and captures you.")

def throne_room():
	print "You enter a grand throne room."
	print "Good thing you stole that guard uniform." 
	print "Nobody suspectes a thing."
	print """
	There a two clear ways out of the throne room.
	One leads to the stables and the other to the courtyard. 
	What do you choose?

	A. Stables
	B. Courtyard
	"""		

	choice = raw_input(prompt)
	if choice == "a":
		stables()
	elif choice == "b":
		courtyard()
	else:
		dead("You have been discovered.")

def courtyard():
	print "You set foot in the courtyard and notice it still dark out"
	print"...this is good. Hopefully you wont be noticed."
	print "Quietly you make your way across the yard when a voice calls to you."
	sleep(3)
	print """
	Hey you! Stop there!
	...I thought I locked you away in the dungeons!
	"""
	print "You turn to see the man that captured you charging toward you."
	sleep(2)
	print """
	What do you do?
	1. Attack!
	2. Flee!
	3. Climb the ladder to your left.
	"""
	choice = int(raw_input(prompt))
	if choice == 1:
		print "You meet your foe in the courtyard and attack"
		critical_hit = random.randint(1, 6)
		print "Your chance of landing is critical hit is %d" % critical_hit
		if critical_hit >=3:
			print "You strike down your foe. Killing him."
			print "You stand and run to the stables"
			stables()
		else:
			dead("You are defeated in the courtyard.")
	elif choice == 2:
		dead("you are too tired to out run him and are easily captured.")
	elif choice == 3:
		moat()
	else:
		dead("You are recaptured")

def moat():
	print "You climb the ladder and stand atop the wall."
	print "behind you your foe is climbing after you"
	print "infront of you is a sheer drop into the ocean."
	print "Do you fight or jump?"
	choice = raw_input(prompt)	
	if "jump" in choice :
		print "You leap off the wall."
		survival = random.randint(1,6)
		print "Your chance of survival is %d" % survival
			
		if survival >= 3:
			freedom("You land in the river and swim to shore.")
		else:
			dead("You do not survive the fall.")
		
	elif "fight" in choice:
		dead("You are too tired to fight and are recaptured.")

	else:
		dead("You are recaptured")		


def stables():
	print "Out of breath you slip into the stables."
	print "A the stables are quiet and there are 3 horses available."
	sleep(2)
	print """

	Which do you do?

	1. Black Garron 
	2. White Charger
	3. Old Destier

	"""
	choice = int(raw_input(prompt))

	if choice == 1:
		dead("The horse is too wild and throws you from the saddle")
	elif choice == 2:
		dead("The horse is unruly makes a fuss. This attracts the attention of guards. ")
	elif choice == 3:
		freedom("The old horse leads you to safety.")

def dead(why):
	print why, "You failed to escape"
	print "Want to play again?"
	print "Y or N"

	cont = raw_input(">")
	if cont == "y":
		print "Very Well..Good luck"
		sleep(3)
		dungeon()
	else:
		print "GAME OVER"
		exit(0)

def freedom(why):
	print why, "YOU HAVE ESCAPED THE CASTLE!"
	print "Want to play again?"
	print "Y or N"

	cont = raw_input(">")
	if cont == "y":
		print "Very Well..Good luck"
		sleep(3)
		dungeon()
	else:
		print "GAME OVER"
		exit(0)

dungeon()
	