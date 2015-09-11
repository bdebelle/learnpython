# Define function named  Cheese and Crackers with 2 arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man thats enough for a party!"
	print "Get a blanket.\n"

# gives values directly to the function for its 2 arguments
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# back to basics, set variables and insert them in the function
print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Setting arguments as equations
print "We can even do the math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# arguments as variables from above combined with math
print "And we can even combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
