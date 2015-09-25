# Set variables equal to integers
people = 30
cars = 40
buses = 15

if cars > people:
	# 40 > 30 is true so this will print and elif / else
	# will be skipped
	print "We should take the cars."
elif cars < people:
	print "We should take the cars."
else:
	print "We can't decide."

if buses > cars:
	# 15 > 40 is False so this will not be printed
	print "Thats too many buses."
elif buses < cars:
	# 15 < 40 is true so this will print and "else"
	# will be skipped
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

if people > buses:
	# 30 > 15 is true so this will print and 
	# else will be skipped
	print "Alright, lets just take the buses."
else:
	print "Fine, Let's stay home then."

# Elif stands for "else if" and its used for 
# additional condition, while "else" is used to cover
# anything not specifically addressed 

if cars != buses and people > cars:
	print "We probably have to take the shitty buses."
else:
	print "Hey where the fuck are we going anyway?"