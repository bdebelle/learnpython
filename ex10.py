tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat



my_name = "Brian \"The Man\" DeBelle"

print "let's talk about %r" % my_name
print "let\'s \\ talk \\ \"about\" \'%s\'" % my_name

joke_evaluation = "Isnt that joke... \nfunny? %r"
hilarious = "not \nreally"

print joke_evaluation % hilarious

joke_evaluation = "Isnt that joke...funny? %r"
hilarious = "\nnot \nreally"

print joke_evaluation % hilarious


