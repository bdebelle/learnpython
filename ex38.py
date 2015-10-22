# Doing things to lists
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

# Variable equal to ten_things with list items split by a space.
# ['Apples', 'Oranges', 'Crows', 'Telephone', 'light', 'sugar']
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: # Run this loop until 10 items are in the list 'stuff'
	next_one = more_stuff.pop() # will take the last item of more_stuff and set it equal to variable next_one
	print "Adding: ", next_one # prints what item will be added to list
	stuff.append(next_one) # Appends current item equal to variable 'next_one' to the list 'stuff'
	print "There's %d items now." % len(stuff) # print current length of the list 'stuff'

print "There we go: ", stuff # print final form of list 'stuff' 

print "Let's do some things with stuff."

print stuff[1] # Print item in the list stuff at cardinal position 1 
print stuff[-1] #Pulls from the End of the list
print stuff.pop() # Remove the item at the given position and return it
print ' '.join(stuff) # Take all the items in the list 'stuff' and join them with a space
print '#'.join(stuff[3:5]) #Take Items in cardinal positons 3 & 5 and join them together with a #
