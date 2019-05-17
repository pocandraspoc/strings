import unittest
# UNTIL THE LINE THIS IS MY TERRITORY DO NOT EVEN THINK ABOUT TO EDIT THIS PART
class test_consonant(unittest.TestCase):
	"""docstring for test_consonant"""
	def test_upper(self):
		self.assertEqual('FOO'.upper(), 'FOO')

	def test_consonant(self):
		self.assertEqual(consonant('asztal'), 3)

		
###### YOU CAN TOUCH things ONLY UNDER THIS => __________ <= LINE!!

def consonant(string: str) ->int:
	"""
	"""
	return 3

if __name__ == '__main__':
    unittest.main()
