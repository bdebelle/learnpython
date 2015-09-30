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
		print "At the top i is %d" % i
		this_list.append(i)

		i = i + 1
		print "Numbers now: %d" % i
	print this_list 

print "\nNow calling function sd1 with the value of n = 3"
sd1(3)
print "\nNow calling function sd1 with the value of n = 9"
sd1(9)

print "\nPassing in the Variable step in function sd3"

def sd3(n, step):
	i = 0
	this_list = []
	while i < n:
		print "At the top i is %d" % i
		this_list.append(i)

		i = i + step
		print "Numbers now: %d" % i
	print this_list

print "\nCalling function sd3 with n = 10 and step = 2"
sd3(10, 2)


print "\nWriting function sd5 to use for-loop and range"

def sd5(n, step):
	numbers = range(0, n, step)
	for i in numbers:
		print "item is number: %d" % i

sd5(21, 3)
