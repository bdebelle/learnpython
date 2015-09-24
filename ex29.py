people = 20 
cats = 30
dogs = 15

if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "the word is drooled on!"

if people > dogs:
	print "The world is dry!"


dogs += 5
# This is a shortcut of saying dogs = dogs + 5

if people >= dogs:
	print "People are greater than or equal to dogs."

if people <= dogs:
	print "People are less than or equal to dogs."


if people == dogs:
	print "People are dogs"

## Study Drills ##
# 1. What do you think the "if" does to the code under it?
# 1A. if the value is true it will trigger the funtion underneath it. 
# 2. Why Does the code under the "if" need to be indented four spaces?
# 2A. To create a block. Local vs Global?
# 3. What happens if it isnt indented?  
# 3A. IndentationError
# 4. Can you put other boolean expressions from exercise 27 in the if-statement?
# 4A. Yes. 
# 5. What happens if you change the initial variables for People, Cats, and dogs?
# 5A. A different If statement is triggered

#Extra Credit
if people == dogs or people != cats:
	print "People are dogs"

if people == dogs and cats != people:
	print "People are super-duper"

