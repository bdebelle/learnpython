import time

print "\nFor Loop"
elements = range(0,6)
for i in elements:
	print "Elements item id is: %d" % i

for letter in "Python":
	print 'Current letter: ', letter

print "\nWhile Loop"
import time


for num in range(10, 20): # to iterate between 10 and 20
	for i in range(2, num): # to iterate on the factors of the numbers
		if num % i == 0: # to determine the first factor
			j = num / i # to calculate the second factor
			print "%d equals %d * %d" % (num,i,j)
			break # to move ot the next number, The first for
	else: # else part of the loop
		print num, 'is a prime number'

print "\nThis message Will self destruct in:"
i = 3
lists = []	
while i > 0 :
	lists.append(i)
	i = i - 1
	print " %d" % i
	time.sleep(1) # will delay printing for 1 second
	

print "*#*poof*#*"

print lists
