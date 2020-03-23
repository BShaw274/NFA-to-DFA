"""

"""
import json

#DFA Class
class DFA:
	"""Represents a DFA internally
	
	Attributes:
		alphabet (list): The DFA's alphabet
		states (list): The DFA's states
		initial_state (int): The DFA's initial state
		delta (list[list]): The DFA's function which is contained as a states table
		final_states (list): The DFA's final states which validites or denies the input
		
		
	"""
	def __init__(self, alphabet, states, initial_state, delta, final_states):
		"""Creates a new DFA
		
		Args:
			alphabet (list): The DFA's alphabet
			states (list): The DFA's states
			initial_state (int): The DFA's initial state
			delta (list[list]): The DFA's function which is contained as a states table
			final_states (list): The DFA's final states which validites or denies the input
			current_state (int): The DFA's current state which is initialized at initial state
		Returns:
			DFA: The created DFA
		"""
		self.alphabet = [str(i) for i in alphabet]
		self.states = states
		self.initial_state = initial_state
		self.delta = delta
		self.final_states = final_states
		self.current_state = initial_state
	def is_in_alphabet(self, value):
		"""Tests if the value is in the alphabet
		Args:
			value: A value being tested if in alphabet

		Returns:
			bool: If the value is a part of the alphabet
		"""

		return value in self.alphabet

	def transition(self, value):
		"""Transitions current state to next state depening on value and updates it internally
		Args:
			value: A value from the alphabet that determines the next state
		"""
		self.current_state = self.delta[self.current_state][self.alphabet.index(value)]

	def peak(self, value):
		"""Peaks at the next state according to the value
		Args:
			value: A value from the alphabet that determines the next state
		returns:
			int: This is the next state according to the value
		"""
		return self.delta[self.current_state][self.alphabet.index(value)]

	def if_accepted_state(self):
		"""Tests if the current state is an acceptable final state
		Returns:
			bool: If the current state is an acceptable final state
		"""
		return self.current_state in self.final_states




#Main

"""

"""
if __name__ == "__main__":
	with open('NFAtoDFA.json', 'r') as f:
		data = f.read()
		
	#print("This is the DFA Definition")
	#print(data)
	data = json.loads(data)

	place_holder = DFA(**data)

	userin = "abab"

	for i in userin:
		if place_holder.is_in_alphabet(i) == False:
			print("ERROR: NOT VALID INPUT")

	for i in userin:
		place_holder.transition(i)

	print (place_holder.if_accepted_state())