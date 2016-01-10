#All 3 combined
# Create a class named Parent that is a object
class Parent(object):

	#class Parent has-a override funtion that takes self parameters
	def override(self):
		print "PARENT override()"
	#class Parent has-a implicit funtion that takes self parameters
	def implicit(self):
		print "PARENT implicit()"
	#Class Parent has-a altered function that takes self parameters
	def altered(self):
		print "PARENT altered()"

#Create a class names Child that is-a Parent
class Child(Parent):
	# this line overrides the parent function override
	def override(self):
		print "CHILD override()"
	#this funcntion overides the parent function alterd
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		# Call super arguement with chilc and self, then call the funtion altered on what it returns
		super(Child, self).altered()
		#this overides the parent funtionaltered
		print "Child, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
