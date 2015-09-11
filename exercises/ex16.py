# import argv module from the system
from sys import argv
# setting the argument variables
script, filename = argv
# asking for user input on keeping the file	
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)." # interupts script
print "If you do want that, hit RETURN." # Proceeds with script

raw_input("?") # asking for user input

print "Opening the file..."
target = open(filename, 'w') # open file in 'w' mode WRITE MODE

print "Truncating the File. Goodbye!"
# empties the file
# target.truncate()

# print "Now I am going to ask you for three lines."
# raw user input that will be placed in our now empty file
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
# Writes the raw inputs to the file and separates them one lines. 

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
# ^^ much more efficient than vv

'''
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
'''

# close and saves file. 
#print "And finally, we close it."
#target.close()

## THIS IS MY STUDY DRILL SCRIPT
print "we are going to read some files like %r." % filename
print "Hit RETURN to continue."

raw_input("> ")

print "Translating...Beep.Boop.Bee.Bop"
target = open(filename, 'r')
print target.read()

print "Everyting look ok here?"

raw_input(">")

print "lets close this thing"
target.close()
