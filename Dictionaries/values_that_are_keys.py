def values_that_are_keys(my_dictionary):
  vk = []
  for value in my_dictionary.values():
    if value in my_dictionary.keys():
      vk.append(value)
  return vk
#print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
#print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]