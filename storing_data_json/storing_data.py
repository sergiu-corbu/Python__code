'''
store data with json
import json
#write data with json.dump
numbers = [2,3,4,5]
filename = 'storing_data_json/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers,f)

#read data  w/ json.load
with open(filename) as f:
    numbers = json.load(f)
print(numbers)

#saving and reading user-generated data
username = input("what is your name?")
filename = 'storing_data_json/username.json'
with open(filename,'w') as f:
    json.dump(username,f)
    print(f"We will remember you when you come back, {username}")

with open(filename) as f:
    username  = json.load(f)
    print(f"Welcome back, {username}")
'''
#final program
import json

filename = 'storing_data_json/username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("Please enter your name ")
    with open(filename, 'w') as f:
        json.dump(username,f)
        print(f"We ll remember you, {username}")
else:
    print(f"welcome back, {username}")
