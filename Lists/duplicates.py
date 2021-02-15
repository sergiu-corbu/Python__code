# remove duplicates 
# no time/space requirements
# return a list with duplicates removed

def remove_duplicates1(dupe_list):
  unique_values = []
  for el in dupe_list:
    if el not in unique_values:
      unique_values.append(el)
  return unique_values

#optimized 

def move_duplicates(dupe_list):
  unique_idx = 0
  for i in range(len(dupe_list) - 1):
    if dupe_list[i] != dupe_list[i + 1]:
      dupe_list[i], dupe_list[unique_idx] = dupe_list[unique_idx], dupe_list[i]
      unique_idx += 1
  dupe_list[unique_idx], dupe_list[len(dupe_list) - 1] = dupe_list[len(dupe_list) - 1], dupe_list[unique_idx]
  return unique_idx


#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(remove_duplicates(['a', 'a', 'x', 'x', 'x', 'g', 't', 't']), ['a', 'x', 'g', 't'], remove_duplicates(['a', 'a', 'x', 'x', 'x', 'g', 't', 't']) == ['a', 'x', 'g', 't']))

print("{0}\n should equal \n{1}\n {2}\n".format(remove_duplicates(['c', 'c', 'd', 'd', 'e', 'e', 'f', 'a', 'a']), ['c', 'd', 'e', 'f', 'a'], remove_duplicates(['c', 'c', 'd', 'd', 'e', 'e', 'f', 'a', 'a']) == ['c', 'd', 'e', 'f', 'a']))

print("{0}\n should equal \n{1}\n {2}\n".format(remove_duplicates([13, 13, 13, 13, 13, 42]), [13, 42], remove_duplicates([13, 13, 13, 13, 13, 42]) == [13, 42]))