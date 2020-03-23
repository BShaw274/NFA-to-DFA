import json

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

	#print(data["final_states"])
	print(new_states)
	for i in range(len(new_states)):
		print(i)
		for j in range(len(initial_final_states)):
			if initial_final_states[j] in new_states[i]:
				final_states.append(new_states[i])
	print(final_states)
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
#Main

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
	#print("states", list(enumerate(states)))
	#print("delta", list(enumerate(delta)))

	return delta, states

if __name__ == "__main__":
	with open('binaryTestNFA.json', 'r') as f:
		data = f.read()
	data = json.loads(data)
	states = []
	delta = []
	final_states= []

	delta,states = translate(data)
	final_states = final_states_finder(data, states)

