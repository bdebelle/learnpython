name = 'Brian J. DeBelle'
age = 26 #not a lie
height = 70.0 # inches
weight = 190.0 #lbs
eyes = 'Brown'
teeth = 'white'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d punds heavy." % weight
print "Actually thats no too heavy." 
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)

cm = height * 2.54
kilo = weight * .4536

print "His height in centimeters is %f" % cm
print "His weight in kilograms is %f" % kilo