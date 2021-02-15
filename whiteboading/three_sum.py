'''a general harder problem
given an array nums of n integers, are there elements a,b,c such their sum is 0?
inputs: an array of numbers
output: an array of triples of numbers
edge cases: none of the numbers sum to 0
 
assumptions: input can  have duplicates
            output numbers MUST be unique
            triplets order does not matter

#naive solution -  3 for loops -> not optimal 

better solution: .sort() , intelligent traversal
starting with the leftmost negative number, at index i, make j = nums[i+1] and k = nums[len(nums)-1] and 
apply the palindrome method, to see which numbers add to 0

time complexity: sorting + inner + outer loop
                 nlogn + n + n -> nlogn + n**2 -> n**2
space complexity: output array: o(n)
'''

def threeSum(nums):
    output = []
    nums.sort()
    length = len(nums)
    for i in range(length):
        left, right = i + 1, length - 1 
        #to avoid duplicates solutions, manually move the base pointer, like a skip
        if i > 0 and nums[i-1] == nums[i]: continue
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                output.append([nums[i], nums[left], nums[right]])
                #the same issue, skip the duplicates
                while left < right and nums[left + 1] == nums[left]:
                    left += 1
                while left < right and nums[right -1] == nums[right]:
                    right -= 1
                left += 1
                right -= 1
            elif total > 0:
                right -= 1
            else:
                left += 1
    return output

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))