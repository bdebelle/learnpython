# Importing argv from the sys module
from sys import argv
# Sets up script for one parameter
script, input_file = argv
# define a function to print contents of file object f
def print_all(f):
	print f.read()
# define a function to move the cursor to the first position 
# of file object f
# ie byte 0
def rewind(f):
	f.seek(0)
# define a function to print the contents of a specific 
# line of file object f and number of its line 
# f is our object from above and readline is a
# built in function
def print_a_line(line_count, f):
	print line_count, f.readline()
# open the passed file and assign it to a variable
current_file = open(input_file)
# print string
print "First let's print the whole file:\n"
# send file to print_all function
print_all(current_file)
# print string
print "Now lets rewind, kind of like a tape."
# send file to rewind function
rewind(current_file)
# print string
print "Let's print three lines:"
# index current line
current_line = 1
# send current line and file to print_a_line function
#current line = 1
print_a_line(current_line, current_file)
# increment curent_line by one
current_line += 1
# send current line and file to print_a_line function
# current line = 2
print_a_line(current_line, current_file)
# increment curent_line by one
current_line += 1
#send current line and file to print_a_line function
# current line = 2
print_a_line(current_line, current_file)
