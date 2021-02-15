'''
enumerate() is used when we need the index of that item, not only the value
so there will be 2 variables for both items

'''

letters = ['a', 'b', 'c', 'd']

#standard loop for values
for letter in letters:
    print(letter)

#loop for the index and the value
for index in range(len(letters)):
    print('letters ', index, '=', letters[index])

#a better way, enumerate function will return a tuple
for index, item in enumerate(letters):
    print('letters ', index, '=', item)
#or
enum_obj = enumerate(letters)
print(next(enum_obj))
print(next(enum_obj))
print(type(enum_obj))

