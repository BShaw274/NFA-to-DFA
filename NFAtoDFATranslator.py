import json
import sys

#examples https://www.cs.wcupa.edu/rkline/fcs/nfas.html

def compile_NFA_to_DFA(alphabet, initial_state, delta, states, final_states):
	"""This is to compile the translated NFA into a DFA format
	Args:
		alphabet (list): All the accepted characters in the language
		initial_state (list): The starting start of the NFA
		delta (list): The function that decides which state to go to
		states (list): A list of all of the new states that are needed for the DFA
		final_states (list): All the final states that validate an input
	"""
	data = dict()
	data["alphabet"] = alphabet
	data["states"] = states
	data["initial_state"] = initial_state
	data["delta"] = delta
	data["final_states"] = final_states


	data = json.dumps(data)
	with open('NFAToDFA.json', 'w') as f:
		f.write(data)

def cleans_states(states, delta, final_states):
	"""Indexes the states such that the DFA reader will be able to use them
	Args:
		states (list): The NFA states that have been translated
		delta (list): The DFA states that have been translated
		final_states (list): The DFA final states
	Returns:
		delta (list): The delta now cleaned with states as individual numbers
		states (list): Now a list of states that works as an index
		final_states (list): The clean states now

	"""
	for i in range(len(delta)):
		for j in range(len(delta[i])):
			index = states.index(delta[i][j])
			delta[i][j] = index
	for i in range(len(final_states)):
		index = states.index(final_states[i])
		final_states[i] = index

	states = range(len(states))
	return delta, list(states), final_states


def final_states_finder(data, new_states):
	"""Takes in the new states and locates where the new final states will be
	Args:
		data (dict): The NFA definition
		new_states (list): List of the NFA states translated into the DFA states
	Returns:
		list: The new final states
	"""
	final_states = []
	initial_final_states = data["final_states"]

	for i in range(len(new_states)):
		for j in range(len(initial_final_states)):
			if initial_final_states[j] in new_states[i]:
				final_states.append(new_states[i])
	return final_states

def epsilon_grouping(data, state):
	"""Recursively finds all the states reachable from the given
	state by epsilon transition

	Args:
		data (dict): The NFA definition
		state (int): The state to start at
	Returns:
		list: The reachable states
	"""
	states = [state]
	if state is None:
		return [None]
	for j in data["e"][state]:
		states += epsilon_grouping(data, j)
	return states

def explore_for_character(data, state, character):
	"""Gets all states reached when the given character is inputted
	and the nfa is at the given state

	Args:
		data (dict): The NFA definition
		state (list[int]): The non-deterministic state to check at
		character (str): The character to input to the machine
	Returns:
		Returns a list of the reached states
	"""
	result = []
	alphabet_index = data['alphabet'].index(character)
	for i in state:
		if i is None:
			result += [None]
		else:
			result += epsilon_grouping(data, data['delta'][i][alphabet_index])
	return result

def explore(data, state):
	"""Gets the transitions for each letter in the alphabet
	when the NFA is in the given state

	Args:
		data (dict): The definition of the NFA
		state(list[int]): The non-deterministic state of the NFA
	Returns:
		list[list]: The transitions based on the index of the letters of the alphabet
			NOTE: Will remove excess None's
	"""
	result = []
	for i in data['alphabet']:
		temp = explore_for_character(data, state, i)
		if None in temp:
			while None in temp:
				temp.remove(None)
			if len(temp) == 0:
				temp.append(None)
		result.append(temp)
	return result

def translate(data):
	"""This function translates the function into the new states and new mapping for the states

	Args:
		data (dict): The definition of the NFA

	"""
	states = [epsilon_grouping(data, data['initial_state'])]
	states_to_create = explore(data, states[0])
	delta = []
	delta.append(explore(data, states[0]))
	while states_to_create:
		next_state = states_to_create.pop()
		states.append(next_state)
		new_delta = explore(data, next_state)
		delta.append(new_delta)
		for i in new_delta:
			if (i not in states_to_create and i not in states):
				states_to_create.append(i)

	return delta, states

if __name__ == "__main__":

	#this is where you change the json
	nfa = sys.argv[1]
	print(nfa)
	with open(nfa, 'r') as f:
		data = f.read()
	data = json.loads(data)
	states = []
	delta = []
	final_states= []
	

	initial_state = data["initial_state"]
	delta,states = translate(data)
	final_states = final_states_finder(data, states)
	alphabet = data["alphabet"]
	delta,states,final_states = cleans_states(states, delta, final_states)

	compile_NFA_to_DFA(alphabet, initial_state, delta, states, final_states)