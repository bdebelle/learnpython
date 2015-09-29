i = 0
numbers = [ ]

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
print "The numbers: "

for num in numbers:
	print num

print "\nConvert while-loop to a function and replace 6 in the test with a variable"


def sd1(n):
	i = 0
	this_list = []
	while i < n:
		print "Item: %d" % i
		this_list.append(i)

		i = i + 1
		print "Item now: %d" % i
	print this_list

print "\nCalling sd1 with n = 5"
sd1(5)

print "\nCalling sd1 with n = 9"
sd1(9)

print "\nAdding variable that will allow me to change the increment 'step'"

def sd3(n, step):
	i = 0
	this_list2 = []
	while i < n:
		print "Item is: %d" % i
		this_list2.append(i)
		i = i + step
		print "Item is now: %d" % i
	print this_list2

print "\nCalling function sd3 with n = 10 and step = 2"
sd3(10, 2)

print "\nCalling function sd3 with n = 12 and step = 3"
sd3(12, 3)

print "\nUsing For-loops and range in sd3"
def sd5(n, step):
	numbers5 = range(0, n, step)
	for i in numbers5:
		print "item is: %d" % i
	print numbers5

sd5(21, 3)





