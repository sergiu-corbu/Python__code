# find rotation point 
# O(logN) time requirement
# return index of "rotation point" element

def rotation_point(rotated_list):
  n = len(rotated_list)
  rpoint = 0
  low = 0
  high = len(rotated_list) - 1
  while low < high:
    mid = (low + high)/2
    mid_next = (mid+1) % n
    mid_prev = (mid-1) % n
    if mid < mid_next and mid < mid_prev:
      rpoint = mid
    else:
      if rotated_list[mid] < rotated_list[high]:
        high = mid - 1
      else:
        low = mid + 1
  return rpoint

def rotation_point(rotated_list):
  low = 0
  high = len(rotated_list) - 1
  while low <= high:
    mid = (low + high) // 2
    mid_next = (mid + 1) % len(rotated_list)
    mid_previous = (mid - 1) % len(rotated_list)
    
    if (rotated_list[mid] < rotated_list[mid_previous]) and (rotated_list[mid] < rotated_list[mid_next]):
      return mid
    elif rotated_list[mid] < rotated_list[high]:
      high = mid - 1
    else:
      low = mid + 1






#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['a', 'b', 'c', 'd', 'e', 'f']), 0, rotation_point(['a', 'b', 'c', 'd', 'e', 'f']) == 0))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['c', 'd', 'e', 'f', 'a']), 4, rotation_point(['c', 'd', 'e', 'f', 'a']) == 4))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point([13, 8, 9, 10, 11]), 1, rotation_point([13, 8, 9, 10, 11]) == 1))