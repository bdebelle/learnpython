## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		##Dog has-a variable name 
		self.name = name

# Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		#Cat has-a variable name
		self.name = name

# Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a variable name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		#The class Employee inherits something from Person
		super(Employee, self).__init__(name)
		##Employee has-a variable Salary
		self.salary = salary

# Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

# Mary has-a pet called satan
mary.pet = satan

## Frank is-a Employee
frank = Employee("Frank", 120000)

## Frank has-a pet called rover
frank.pet = rover

## Flipper is-a instance of class Fish
flipper = Fish()

## crouse is-a instance of class Salmon	
crouse = Salmon()

## harry is-a instance of class Halibut
harry = Halibut()



