# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  result = {}
  for item in words:
    if item not in result.keys():
      result[item] = 1
    elif item in result.keys():
      result[item] += 1
  return result
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}



#unique values

# Write your unique_values function here:
def unique_values(my_dictionary):
  unique = []
  for value in my_dictionary.values():
    if value not in unique:
      unique.append(value)
  return len(unique)
# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1