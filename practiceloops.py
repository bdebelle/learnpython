print "\nFor Loop"
elements = range(0,6)
for i in elements:
	print "Elements item id is: %d" % i

print "\nWhile Loop"
import time

print "\nThis message Will self destruct in:"
i = 10
lists = []

	
while i > 0 :
	lists.append(i)
	i = i - 1
	print " %d" % i
	time.sleep(1) # will delay printing for 1 second
	

print "*#*poof*#*"

print lists