#Alter Before or After
# 3rd way to use inheritance is a special case of overriding where you
# want to alter he behavior before or after the Parent class's version
# runs. You first override the function just like the last (ex44b) example
# but then you use a Python built-in funtion named super to get the Parent
# version to call. 

class Parent(object):

	def altered(self):
		print "PARENT altered()"

class Child(Parent):

	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "Child, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()