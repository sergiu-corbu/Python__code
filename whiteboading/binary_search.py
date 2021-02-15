'''
given a sorted array and a target value, return the index
if the target is found
assumptions: no duplicate values, no empty array
time complexity: O(logn)
'''

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_val = nums[mid]
        if target == mid_val:
            return mid
        elif target > mid_val:
            left = mid + 1
        else:
            left = mid - 1
    return -1

nums = [1,2,5,7,9,52,90,9000,10000,8000000]
print(binary_search(nums, 10000))