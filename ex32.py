the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quaters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

#same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

#also we can go through mixed lists too
#notice we have to use %r since we dont know what's in it
for i in change:
	print "I got %r" % i

# We can also build lists, first start with an empty one 
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list" % i
	# append is a function that lists understand.
	elements.append(i)

#now we can print them out too
for i in elements:
	print "Elements was: %d" % i

# Range function
"""
range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers
    
    Return a list containing an arithmetic progression of integers.
    range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
    When step is given, it specifies the increment (or decrement).
    For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
    These are exactly the valid indices for a list of 4 elements.
    """
elements2 = range(6)
for i in elements2:
	print "Elements2 item was: %d" % i