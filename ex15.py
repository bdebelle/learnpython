# Imports the arguement variable module from system
from sys import argv
# set are argument variables
script, filename = argv
# variable txt set to open variable filename
txt = open(filename)
# print string with Repr File name
print "Here's your file %r:" % filename
#Prints the contents of TXT which is set to open variable filename
print txt.read()
# String
print "type that file name again:"
# variable = to raw use input with arrow prompt
file_again = raw_input("> ")
# variale set to open the contents on variabel
#file_again which is a user input
txt_again = open(file_again)
# Print variable  which is given the command to
# read contents of user raw input
print txt_again.read()
txt.close()
txt_again.close()