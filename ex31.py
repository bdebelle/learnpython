print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	print "3. Leave the room."

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	elif bear == "3":
		print "Wow, That was a close one! what do you want to do about the bear?"
		print "1. lock the door and throw away the key."
		print "2. Burn this place to the ground."

		action1 = raw_input("> ")

		if action1 == "1":
			print "You have trapped the bear!"
		elif action1 == "2":
			print "Yeah... Fuck that bear"
		else: 
			print "Doing %s is a good choice I guess. " % action1
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	print "4. Talk to the man in the black coat."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives, powered by a mind of jello. Good Job!"
	elif insanity == "4":
		print "You are met by a man who intorduced himself as 'Morpheus'..."
		print """ This is your last chance.\nAfter this, there is no turning back.\nYou take the blue pill\n -- the story ends, you wake up in your bed and believe whatever you want to believe.\nYou take the red pill\n -- you stay in Wonderland and I show you how deep the rabbit hole goes.
		"""
		pill = raw_input("blue or red?> ")

		if pill == "blue":
			print "You wake up in your bed, feeling as if youve had the strangest dream."
		elif pill == "red":
			print "Welcome to the Nebuchadnezzar, Neo."
		else:
			print "You took too long... Agent Smith finds you and kills you."
	else:
		print "The insanity rots your eyes into a pool of muck. Good Job!"

	
else:
	print "You stumble around and fall on a knife and die. Good job!"










