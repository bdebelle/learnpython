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