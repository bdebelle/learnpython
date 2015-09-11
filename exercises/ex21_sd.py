def money(a, b):
	return a + b

def debt(a, b):
	return a - b

money_in_bank = money(100, 300)

debts_owed = debt(300, 100)

finances = money(money_in_bank, debt(debts_owed, money_in_bank))

print "You are worth", finances, "dollars."

# finances = money(money_in_bank, debt(debts_owed, money_in_bank))
# finances = money(400, debt(200, 400)
# finances = money(400, (-200))
# finances =  400 + (-200)
# finances = 200



# THE DUMB FUCKING PUZZLE
# Study drill 2
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# what = add((30 +5), subtract((78-4), multiply((90*2), divide(100/2), 2)))
# what = add((35), subtract((74), multiply((180), divide(50), 2)))
# what = add((35), subtract((74), multiply((180), 25)))
# what = add((35), subtract((74), 4500))
# what = add((35), -4426)
# what = -4391

#Study Drill #3
number = 8
what2 = add(age, subtract(height, multiply(weight, divide(iq, number))))
print "what change number to %d we get what answer %d" % (number, what2)

#Study Drill #4
what_3 = 5 + (10 - (3 * (4 / 2)))
what_3 = 5 + (10 - (3 * divide(4, 2)))
what_3 = 5 + (10 - multiply(3, divide(4, 2)))
what_3 = 5 + subtract(10, multiply(3, divide(4, 2)))

what_3 = add(5, subtract(10, multiply(3, divide(4, 2))))

print "when I make my own dumb puzzle the answer is %r" % what_3