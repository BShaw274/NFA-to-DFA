import json


with open('binaryTest.json', 'r') as f:
	data = f.read()
print(data)
data = json.loads(data)
print(data["alphabet"])