print "I will now count my chickens:"
# line 3 diveds 30 by 6 and then adds 5 to make 25. line 4 is 100 - ((25 * 3) modulo 4) which works out to 100-(75modulo4) or 100-3 
print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4
#just a statement
print "Now I will count my eggs:"
# this works out to 6.75 using real math but python likes to make it 7 In py2, 1/4->0 for integers, in py3 1/4->0.25. You can use explicit true division in py2
print 3 + 2 + 1 - 5 + (4 % 2 - (1. / 4)) + 6
# this is a string
print "Is it true that 3 + 2 < 5 - 7?"
# this asks python a question, since the 5 is actually greater than -2 python returns the answer "false"
print 3 + 2 < 5 - 7
# adds 3 to 2 and subtracts seven from 5
print "What is 3 + 2?" , 3 + 2 
print "What is 5 - 7?" , 5 - 7 
# this is a string
print "Oh, that's why its False."
# this is a string
print "How about some more."
#Just like above, the following are asking python True or False question with math.
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2 

print 750 / 3 > 1500 / 10 

print 1 / 4
print 1.0 / 4