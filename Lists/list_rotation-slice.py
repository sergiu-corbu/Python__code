# rotate list forward
# no time/space requirements
# return "rotated" version of input list

def rotate(list, k):
    for i in range(k):
        list.insert(0, list.pop())
    return list

def rotate_slice(list, degree):
    rotation = degree % len(list)
    return list[-rotation:] + list[:-rotation]



# rotate list backwards
# Constant space requirement
# return input list "rotated"

def rev(lst, low, high):
  while low < high:
    lst[low], lst[high] = lst[high], lst[low]
    high -= 1
    low += 1
  return lst

def rotate(my_list, num_rotations):
  # first half
  rev(my_list, 0, num_rotations - 1)

  # second half
  rev(my_list, num_rotations, len(my_list) - 1)

  # whole list
  rev(my_list, 0, len(my_list) - 1)
  return my_list


#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1), ['f', 'a', 'b', 'c', 'd', 'e'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1) == ['f', 'a', 'b', 'c', 'd', 'e']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2), ['e', 'f', 'a', 'b', 'c', 'd'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2) == ['e', 'f', 'a', 'b', 'c', 'd']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3), ['d', 'e', 'f', 'a', 'b', 'c'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3) == ['d', 'e', 'f', 'a', 'b', 'c']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4), ['c', 'd', 'e', 'f', 'a', 'b'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4) == ['c', 'd', 'e', 'f', 'a', 'b']))