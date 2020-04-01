This is the NFA to DFA translator and reader for a foundations assignment

HOW IT WORKS:

To achieve the translation this program was written in python for ease
stepping through strings. The NFAtoDFATranslator.py translator will take in a NFA
in a .json format. This is then outputted into a new .json called
NFAToDFA.json which has the machine now in DFA format. Then DFAReader.py with 
read in the .json and take an input file with mutltiple different inputs to test.
This will print "ERROR: NOT VALID INPUT" if a character is not in the 
alphabet. The output will either verify "true" or "false" if the inputted string is a valid
input for the machine.

HOW TO USE IT:
-First: you must run this command to take in the NFA in order to translate it
	example:: python ./NFAtoDFATransator.py test1NFA.json
-Second: you then run the DFA reader with the input file for values to test
	example:: python ./DFAReader.py test1Input.txt

This will then output wether each string is valid or not.

THE THREE TESTS:

1:

the DFA with definition
```json
{
	"alphabet": ["a", "b"],		#this is the alphabet
	"states" : [0,1,2],		#these are all the states
	"initial_state" : 0,		#This is the initial state
	"delta": [[1, null], [null, 2], [0, null]],	#this is the delta that describes state transitions
	"e": [[],[],[0]],		#this describles the epsilon transitions
	"final_states" : [0]		#this is the final states
}
```

the translated DFA from: python ./NFAtoDFATransator.py test1NFA.json
```json
{
	"alphabet": ["a", "b"], 	#the alphabet
	"states": [0, 1, 2, 3, 4], 	#the states
	"initial_state": 0, 		#the initial state
	"delta": [[2, 1], [1, 1], [1, 3], [4, 1], [2, 3]],	#all the deltas and transitions 
	"final_states": [0, 3, 4]	#the final states
}
```
the input values for 1 and the expected values: python ./DFAReader.py test1Input.txt

aba		#True
aa		#False
ab		#True
b		#False
aaa		#False
abab		#True
abababab	#True
ababaababb	#False

2:

the NFA
```json
{
	"alphabet": ["a", "b"],
	"states" : [0,1,2,3,4],
	"initial_state" : 0,
	"delta": [[null, null], [1, null], [3, null],[null, 2], [null, 4]],
	"e": [[1,2],[4],[4],[],[]],
	"final_states" : [4]
}
```
the translated DFA from : python ./NFAtoDFATransator.py test2NFA.json
```json
{
	"alphabet": ["a", "b"], 
	"states": [0, 1, 2, 3, 4, 5, 6, 7, 8], 
	"initial_state": 0, 
	"delta": [[3, 1], [2, 1], [2, 2], [8, 4], [5, 1], [2, 6], [5, 7], [2, 7], [8, 7]], 
	"final_states": [0, 1, 3, 4, 6, 7, 8]
}
```
the input values for 2 and the expected values: python ./DFAReader.py test2Input.txt

a		#True
bb		#True
aa		#True
aaa		#True
ab		#True
aba		#False
abaa		#False
bbba		#False
aaaaaaaaa	#True
aabababab	#False

3:

the NFA
```json
{
	"alphabet": ["0", "1"],
	"states" : [0,1,2,3,4, 5],
	"initial_state" : 0,
	"delta": [[null, null], [3, null], [4, null], [null, 1], [null, 5], [2, null]],
	"e": [[1,2],[],[],[],[],[]],
	"final_states" : [1, 5]
}
```
the DFA translated from: python ./NFAtoDFATransator.py test3NFA.json
```json
{
	"alphabet": ["0", "1"], 
	"states": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
	"initial_state": 0, 
	"delta": [[2, 1], [1, 1], [1, 3], [4, 1], [7, 5], [6, 1], [1, 5], [1, 8], [9, 1], [7, 1]], 
	"final_states": [0, 3, 3, 5, 8]
}
```
the input values for 3 and the expected values: python ./DFAReader.py test3Input.txt

01		#True
00		#False
01010101	#True
010		#False
00110		#False
11001		#False
100101		#False
10101010101	#False


