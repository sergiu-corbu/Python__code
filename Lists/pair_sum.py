# pair sum
# linear time, linear space requirement
# return list of indices that sum to target

def pair_sum(nums, target):
  complements = {}
  indices = {}
  for i in range(len(nums)):
    x = complements.get(nums[i], None)
    if x is not None:
      return [indices[x], i]
    complements[target - nums[i]] = nums[i]
    indices[nums[i]] = i


#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal any of \n{1}\n {2}\n".format(pair_sum([1, 2, 3, 4, 5], 6), [[1, 3], [0, 4]], pair_sum([1, 2, 3, 4, 5], 6) in [[1, 3], [0,4]]))

print("{0}\n should equal any of \n{1}\n {2}\n".format(pair_sum([-1, -1, -2, -4, -5, -9, -12, -13], -21), [[5, 6]], pair_sum([-1, -1, -2, -4, -5, -9, -12, -13], -21) in [[5, 6]]))

print("{0}\n should equal \n{1}\n {2}\n".format(pair_sum([1, -7, 2, 15, -11, 2], 42), None, pair_sum([1, -7, 2, 15, -11, 2], 42) == None))

print("{0}\n should equal any of \n{1}\n {2}\n".format(pair_sum([0, -7, 2, 15, -11, 2], 2), [[0, 2], [0,5]], pair_sum([0, -7, 2, 15, -11, 2], 2) in [[0, 2], [0, 5]]))