#from sys import argv
#script, filename = argv


def finances(money_in_bank, debt_owed):
	print "You have $%d dollars in the bank." % money_in_bank
	print "You owe $%d to the Mafia." % debt_owed
	if money_in_bank > debt_owed: 
		print "You're Fine\n";
	else:  
		print "Better watch out, or you'll be sleepin' with the fishes\n"
	
#1		
finances(9,0)

#2
cash = 1000
mafia_money = 5000

finances(cash, mafia_money)

#3
finances(1000 % 5 + 600, 50 * 8)

#4
finances(cash * 50, mafia_money - 100)

#5
print "How much money do you have?"
money_in_bank = int(raw_input(":$"))
print "How much money do you owe?"
debt_owed = int(raw_input(":$")) 

finances(money_in_bank, debt_owed)

#5 consolidated
print "How much do you have vs how much you owe?"
finances(int(raw_input(":$")) , int(raw_input(":$")))

finances(money_in_bank, debt_owed)

#6
def balance(*args):
	money_in_bank, debt_owed = args
	print "You have %d dollars but you owe %d" % (money_in_bank, debt_owed)

balance(money_in_bank, debt_owed)

#7
print "We can now do something called a loop?"
for i in range(3):
	finances(20, 15)
#8

def info(first_name, last_name, home_country, home_state, lang):
	print "These are are things you tell people.\n"
	print "Your First Name is %r." % first_name
	print "Your Last Name is %r." % last_name
	print "Youre home county is %r" % home_country
	print "and you reside in %r" % home_state
	print "you primarily speak %r\n" % lang
	
print "PLEASE ANSWER THE FOLLOWING QUESTIONS"
info(raw_input("what is your first name?\n"),
raw_input("What is your last name?\n"),
raw_input("What country are you from?\n"),
raw_input("What state do you live in?\n"),
raw_input("What language do you speak?\n"))


