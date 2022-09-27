# must use double quotations

import json # included in standard python
from turtle import clear

# this is a json_string since it is in a python file
# does not the JSON format

json_string = '''
    {
        "students": [
            {
                "id": 1,
                "name": "Tim",
                "age": 21,
                "full-time": true
            },
            {
                "id": 2,
                "name": "Joe",
                "age": 33,
                "full-time": false

            }
        ]
    }
'''

# create our data dictionary
data = json.loads(json_string)
#print(data)
#print(data['students'][0])

# Can dump a Python dictionary into JSON format. 

data['test'] = True # adding a random key to this.
new_json = json.dumps(data, indent = 4, sort_keys= True) # this formats the JSON
print(new_json)

# can load data from a JSON file (r = read)

with open("data.json", "r") as f:
    data = json.load(f)

print(data.items())

# can dump contents of data into data2.json (w = write)

with open("data2.json", "w") as f:
    json.dump(data, f, indent = 4)

# These are instructions for how to save content of JSON into a variable
# and how to save content of variable into a new json