x = "There are %d types of people." %10 # variable x = sting using the decimal formater to call in numbers
binary = "binary" # variable equal to a string
do_not = "don't" # variable equal to a String
y = "Those who konw %s and those that %s." % (binary, do_not) # variable y = string using the string formaters to call upon other variables

print x # print variable x
print y # print variable y

print "I said: %r." % x # print string using the raw formater to call upon raw data in variable x
print "I also said: '%s'." % y # print string using string formater to call upon variable y

hilarious = False # variable equal to false
joke_evaluation = "Isn't that joke so funny?! %r" #variable equal to a string with an undefined raw formater to be set when called upon

print joke_evaluation % hilarious #print variable joke_eval and set previous formater to raw data of variable hilarious

w = "This is the left side of..." # variable equal to a string
e = "a string with a right side." # variable equal to a string

print w + e #print variable w and add e directly to the end of it without a space. (print w,e would look different) 
