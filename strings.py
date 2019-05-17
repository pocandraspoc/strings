import unittest

class test_consonant(unittest.TestCase):
	"""docstring for test_consonant"""
	def test_upper(self):
		self.assertEqual('FOO'.upper(), 'FOO')

	def test_consonant(self):
		self.assertEqual(consonant('ház'), 2)
		self.assertEqual(consonant('lakat'), 3)

def consonant(string: str) ->int:
	"""
	"""
	return 3

if __name__ == '__main__':
    unittest.main()

