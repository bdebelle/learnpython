# Class Hierarchy
# * Map
#	- next_scene
#	- opening_scene	
# * Engine
#	- play
# * Scene
#	- enter
#	* Death
#	* Central Corridor
#	* Laser Weapon Armory
#	* The Bridge
#	* Escape Pod

from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print "Enter is not yet configured"	
		exit(1)

class Engine(object):

	def __init__(self, scene_map, hero):
		self.scene_map = scene_map
		self.hero = hero

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "\n---------"
			next_scene_name = current_scene.enter(self.hero)
			current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

	quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud... If she were smarter.",
		"You died. How many times is this now?",
		"My grandma is better at this than you."
	]

	def enter(self, hero):
		print Death.quips[randint(0, len(self.quips)-1)]
		
		print "Want to play again?"
		print "Y or N"
		cont = raw_input(">")
		
		if cont == "y":
			print "Very Well..Good luck"
			a_game.play()
		
		else:
			print "GAME OVER"
			exit(1)
		

class CentralCorridor(Scene):

	def enter(self, hero):
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew.  You are the last surviving member and your last"
		print "mission is to get the neutron destruct bomb from the Weapons Armory,"
		print "put it in the bridge, and blow the ship up after getting into an "
		print "escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapons Armory when"
		print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
		print "flowing around his hate filled body.  He's blocking the door to the"
		print "Armory and about to pull a weapon to blast you."

		action = raw_input("> ")

		if 'shoot' in action:
			print "Quick on the draw you yank out your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body, which throws"
			print "off your aim.  Your laser hits his costume but misses him entirely.  This"
			print "completely ruins his brand new costume his mother bought him, which"
			print "makes him fly into an insane rage and blast you repeatedly in the face until"
			print "you are dead.  Then he eats you."
			return 'death'

		elif 'dodge' in action:
			print "Like a world class boxer you dodge, weave, slip and slide right"
			print "as the Gothon's blaster cranks a laser past your head."
			print "In the middle of your artful dodge your foot slips and you"
			print "bang your head on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on"
			print "your head and eats you."
			return 'death'

		elif 'joke' in action:
			print "Lucky for you they made you learn Gothon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
			print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
			print "While he's laughing you run up and shoot him square in the head"
			print "putting him down, then jump through the Weapon Armory door."
			return 'laser_weapon_armory'

		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor'

class LaserWeaponArmory(Scene):

	def enter(self, hero):
		print "You do a dive roll into the Weapon Armory, crouch and scan the room"
		print "for more Gothons that might be hiding. Its dead quiet, too quiet."
		print "You stand up and run to the far side of the room and find the"
		print "nuetron bomb in its container. There is a Keypad lock on the box"
		print "and you need the code to get the bomb out. If you get the code"
		print "wrong 10 times the the lock closes forever and you can't"
		print "get the bomb. The code is 3 digits. Dont fuck this up."
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		
		print code

		guess = raw_input("[keypad]> ")
		
		guesses = 1

		while guess != code and guesses < 10:
			print "BZZZZDD!"
			guesses += 1
			guess = raw_input("[keypad]> ")

		if guess == code:
			print "The Container clicks open and the seal breaks, letting the gass out."
			print "You grab the nuetron bomb and run as fast as you can to the"
			print "bridge where you must place it in the right spot."
			return 'the_bridge'
		else:
			print "The lock buzzes one last time and then you hear a sickening"
			print "melting sound as the mechanism is fused together."
			print "You decide to sit there, and finally the gothons blow up the"
			print "ship from thier ship and you die."
			return 'death'

class TheBridge(Scene):

	def enter(self, hero):
		print "You burst on the Bridge with the bomb"

		action = raw_input("> ")

		if action == "throw the bomb":
			print "In a panic you throw the bomb at the group of Gothons"
			print "and make a leap for the door.  Right as you drop it a"
			print "Gothon shoots you right in the back killing you."
			print "As you die you see another Gothon frantically try to disarm"
			print "the bomb. You die knowing they will probably blow up when"
			print "it goes off."
			return 'death'

		elif action == "place bomb":
			print "You point your blaster at the bomb under your arm"
			print "and the Gothons put their hands up and start to sweat."
			print "You inch backward to the door, open it, and then carefully"
			print "place the bomb on the floor, pointing your blaster at it."
			print "You then jump back through the door, punch the close button"
			print "and blast the lock so the Gothons can't get out."
			print "Now that the bomb is placed you run to the escape pod to"
			print "get off this tin can."
			return 'escape_pod'

		else:
			print "Does Not Compute!"
			return 'the_bridge'

class EscapePod(Scene):

	def enter(self, hero):
		print "You rush through the ship desperately trying to make it to"
		print "the escape pod before the whole ship exp[lodes. It seems like"
		print "hardly any Gothons are on the ship, so your run is clear of"
		print "interference.  You get to the chamber with the escape pods, and"
		print "now need to pick one to take.  Some of them could be damaged"
		print "but you don't have time to look.  There's 5 pods, which one"
		print "do you take?"

		good_pod = randint(1,5)

		print good_pod

		guess = raw_input("[pod #]> ")

		if int(guess) != good_pod:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod escapes out into the void of space, then"
			print "implodes as the hull ruptures, crushing your body"
			print "into jam jelly."
			return 'death'
		else:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod easily slides out into the space heading to"
			print "the planet below. As it flies to the planet, you look"
			print "back and see your ship implode then explode like a"
			print "bright star, taking out the Gothon ship and the same"
			print "time. you won!"

			return 'final_fight'

class Final_Fight(Scene):

	def enter(self, hero):

		monster = Monster('Gothon')
		print "%s You have reached the final boss, the Mighty %s! Lets Fight!" % (hero.name, monster.name)

		a_combat = Combat()
		next_stage = a_combat.combat(hero, monster)
		return next_stage



class Finished(Scene):

	def enter(self, hero):
		print "Want to play again?"
		print "Y or N"

		cont = raw_input(">")
		if cont == "y":
			print "Very Well..Good luck"
			a_game.play()
		else:
			print "GAME OVER"
			exit(0)



class Map(object):

	scenes = {
		'central_corridor' : CentralCorridor(),
		'laser_weapon_armory' : LaserWeaponArmory(),
		'the_bridge' : TheBridge(),
		'escape_pod' : EscapePod(),
		'death' : Death(),
		'final_fight' : Final_Fight(),
		'finished' : Finished()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)

	def opening_scene(self):
		return self.next_scene(self.start_scene)




# Returning Next Room?
# Returning the next room as a string assigns this returned value to next_scene_name. We then call the next_scene function and give it the 
# parameter of next_scene_name. The next_scene function looks at scenes dictionary with the next_scene_name as a key and gets the
# corresponding value. The corresponding value is a new instance of the next room, So we create a mew instance of the next room and then 
# call the enter funtion on that room. 


# Build a Simple combat System

class Combat(object):

	def combat(self, hero, monster):
		
		round = 1 
		while True:
			print '='*30
			print "Round %d" % round
			print '='*30
			print "Your HP: %d" % hero.hp
			print "%s's HP: %d" % (monster.name, monster.hp)
			print "Do you wish to attack?"
			print '-'*10
			print "1) Yes Attack!!!"
			print "2) No I'm Scared!"
			
			try:
				action = int(raw_input('> '))
			except ValueError:
				print "Please Enter a Number!"
				continue

			if action == 1:
				hero.attack(monster)

			if action == 2:
				monster.attack(hero)

			if hero.hp <= 0:
				return 'death'

			if monster.hp <= 0:
				return 'finished'

			round += 1

class Human(object):

	def __init__(self, name):
		self.name = name
		
	def attack(self, target):
		target.hp = target.hp - self.atk
		print "%s attacks %s. %s's HP decreased by %d points." % (self.name, target.name, target.name, self.atk)
		return target.hp



class Hero(Human):

	hp = 100
	atk = 15

class Monster(Human):

	hp = 150
	atk = 50



a_map = Map('central_corridor')
a_hero = Hero('Brian')
a_game = Engine(a_map, a_hero)
a_game.play()




