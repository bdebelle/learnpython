from sys import argv

script, filename =argv

print "we are going to read some files like %r." % filename
print "Hit RETURN to continue."

raw_input("> ")

print "Translating...Beep.Boop.Bee.Bop"
target = open(filename, 'r+')
print target.read()

print "Everyting look ok here?"

raw_input(">")

print "lets close this thing"
target.close()
