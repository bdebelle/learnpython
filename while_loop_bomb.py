# Just practicing while loops so i made a countdown
import time

print "\nThis message Will self destruct in:"
i = 10

while i > 0 :
	i = i - 1
	print " %d" % i
	time.sleep(1) # will delay printing for 1 second
	

print "*#*poof*#*"