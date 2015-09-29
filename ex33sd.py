print "\nConverting while-loop to a function drill_1"
def drill_1(n):
	i = 0
	numbers1 = []
	while i < n:
		print "item: %d" % i
		numbers1.append(i)
		i = i + 1
	print numbers1

print "\nUsing dril_1 with n=2"
drill_1(2)

print "\nUsing dril_1 with n=8"
drill_1(8)

print "\nCreating function drill_3 to allow variabale incriment size"
def drill_3(n, s):
	i = 0
	numbers3 = []
	while i < n:
		print "item: %d" % i
		numbers3.append(i)
		i = i + s
		print numbers3
#4 rewrite the script to use the function to what effect it has. 
print "\nUsing drill_3 with n = 12 and s = 3"
drill_3(12, 3)

# 5 write it to use for-loops and range instead. 

print "\ndrill_5 uses a for-loop and range instead"
def drill_5(n, s):
	numbers5 = range(0, n, s)
	for i in numbers5:
		print "item: %d" % i
	print numbers5

drill_5(14, 4)











