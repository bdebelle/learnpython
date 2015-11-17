#########################################
# This is a Script for myself to figure #
# Out how super works.   -BD            #
#########################################

class Person(object):
	def __init__(self, name):

		self.name = name

class Employee(Person):
	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary

f = Employee("Frank", 120000)


print f.name
print f.salary



class Fruit(object):
    def __init__(self, red, yellow):
        self.red = red
        self.yellow = yellow

class Apple(Fruit):
    def __init__(self, red, yellow):
        super(Apple, self).__init__(red, yellow)

a = Apple('blue', 'orange')


print a.red
print a.yellow