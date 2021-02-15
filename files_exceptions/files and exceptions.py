'''
-- files operations: -- 
read 'r', write 'w', append 'a'
with open('filename', 'opperation letter') as ...:
    ..
'''
#--reading from a file--
#reading an entire file
with open('files_exceptions/digits.txt') as file_object:
    contents = file_object.read()
print(contents)

#read line by line
filename = 'files_exceptions/digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)

#making a list of lines from a file
filename = 'files_exceptions/digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

#working with a file's contents
filename = 'files_exceptions/digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
num_string = ''
for line in lines:
    num_string += line.strip()
print(num_string)
print(len(num_string))

#--writing to a file
#writing to an empty file
filename = 'files_exceptions/programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love to code")

#appending to a file !!is the best option over write mode
filename = 'files_exceptions/programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also like finding data models through datasets")

#exceptions
#zero division example
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#using exceptions to prevent crashes
print("give me two numbers and i'll divide them")
print("Enter 'q' to exit")

while True:
    first = input("\nfirst number: ")
    if first == 'q':
        break
    second = input("\n second number: ")
    if second == 'q':
        break
    try:
        answer = int(first) / int(second)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

#handling filenotfound error

filename = 'file.txt'
try: 
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist")

