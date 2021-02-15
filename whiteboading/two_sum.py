'''
given an aray of numbers and a target, return the indices of the number that add up to the numbers
outpot: a tuple consisting of the 2 indices
assumptions: each numbers will appear once and there will always  be a solution
'''

#naive solution, time: O(n*n)
def twoSum(nums, target):
    for i, num in enumerate(nums):
        want = target - num
        for j, other in enumerate(nums[i:]):
            if other == want:
                return [i,j]


#hash table solution, linear time (n)
def twoSum_h(nums, target):
    ht = {}
    for i, num in enumerate(nums):
        want = target - num
        if want in ht:
            left_index = ht[want]
            return [left_index, i]
        else:
            ht[num] = i
        
print(twoSum_h([2,3,4,5], 9))