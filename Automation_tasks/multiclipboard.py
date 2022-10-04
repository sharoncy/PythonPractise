#import modules

import sys # pass commands to 
import clipboard # I installed clipboard to C:\python so had to set interpreter to this too. 
import json

# define an empty json
SAVED_DATA = "clipboard.json"

#print(sys.argv[1:]) # give all the command line arguments that are passed alongside 

# create two functions: 
def save_data(filepath, data): # function for writing a json file
    with open(filepath, "w") as f:
        json.dump(data, f)
        
def load_data(filepath): # function for reading a json file
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {} # if there is no file, return an empty dictionary
        

# define where to get the command from:
if len(sys.argv) == 2: # name of python file then argument
    command = sys.argv[1] # the command is the argument at position 2
 
 #  apply the load_data function to the empty json and tell it what to do based on the command
    data = load_data(SAVED_DATA) # load the data stored in the json
    
    if command == "save": # to save data into the json
        key = input("Enter a key: ") # enter a key
        data[key] = clipboard.paste() #Paste the data under the key
        save_data(SAVED_DATA, data) # save data into json
        print("Data saved!")
    elif command == "load": #
        key = input("Enter a key: ")
        if key in data: 
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("Key does not exist")
    elif command == "list":
        print(data)
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command.")
        

    
# to run, type python multiclipboard.py test in the command line. 
    
