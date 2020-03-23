import unittest
import json
import random
from DFAReader import DFA

class DFATest(unittest.TestCase):
	"""

	"""

	def test_divisible_by_two_or_three_numbers(self):
		"""

		"""
		with open('binaryTest.json', 'r') as f:
			data = f.read()
		data = json.loads(data)

		test_DFA = DFA(**data)

		for i in range(20):
			test_string = ""
			for j in range(i):
				test_string += str(random.choice(data['alphabet']))
			#print("test string", test_string)
		number_of_zeroes = len([i for i in test_string if i == '0'])
		#print("num zeroes", number_of_zeroes)
		expected_value = True if number_of_zeroes % 3 == 0 or number_of_zeroes % 2 == 0 else False

		for i in test_string:
			if test_DFA.is_in_alphabet(i) == False:
				print("ERROR: NOT VALID INPUT")

			for i in test_string:
				test_DFA.transition(i)
		self.assertEqual(test_DFA.if_accepted_state(), expected_value)

	def test_divisible_by_two_or_three_letters(self):
		"""

		"""
		with open('CharacterTest.json', 'r') as f:
			data = f.read()
		data = json.loads(data)

		test_DFA = DFA(**data)

		for i in range(20):
			test_string = ""
			for j in range(i):
				test_string += str(random.choice(data['alphabet']))
			#print("test string", test_string)
		number_of_as = len([i for i in test_string if i == 'a'])
		#print("num zeroes", number_of_zeroes)
		expected_value = True if number_of_as % 3 == 0 or number_of_as % 2 == 0 else False

		for i in test_string:
			if test_DFA.is_in_alphabet(i) == False:
				print("ERROR: NOT VALID INPUT")

			for i in test_string:
				test_DFA.transition(i)
		self.assertEqual(test_DFA.if_accepted_state(), expected_value)


