class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy Birthday to you",
					"I dont want to get sued",
					"So Ill stop right there"])

bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])

thunder_rolls = Song(["Three-thirty in the mornin'",
						"Not a soul in sight"])

thunder = """
City's looking like a ghost town
On a moonlit summer night
"""

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

#study Drill 1
thunder_rolls.sing_me_a_song()

#Study Drill 2

thunder = ["City's looking like a ghost town",
"On a moonlit summer night"]

Song(thunder).sing_me_a_song()
#Pass variable thunder to Class Song and perform function sing_me_a_song