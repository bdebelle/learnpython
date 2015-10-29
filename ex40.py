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

#Study Drill 3

class Track(object):

	def __init__(self, disk):
		self.disk = disk
		self.index = 0
		self.jump()

	def next(self):
		'''jump to next item'''
		self.index = (self.index + 1) % len(self.disk)
		self.jump()

	def prev(self):
		'''jump to previous itme'''
		self.index = (self.index - 1) % len(self.disk)
		self.jump

	def jump(self):
		'''go to item'''
		self.lyrics = self.disk[self.index]

	def sing_song(self):
		for line in self.lyrics:
			print line


track1 = ["Spring Time"]
track2 = ["Summertime"]
track3 = ["its Fall"]
track4 = ["Winter is coming"]

disk = [track1, track2, track3, track4]

mycd = Track(disk)

mycd.sing_song()

mycd.next()
mycd.sing_song()

mycd.next()
mycd.sing_song()

mycd.next()
mycd.sing_song()

mycd.prev()
mycd.sing_song()

mycd.prev()
mycd.sing_song()

mycd.prev()
mycd.sing_song()

mycd.prev()
mycd.sing_song()


	

