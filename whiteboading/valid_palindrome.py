''' 
using pointer method
input: string
output: boolean
edge cases: special carachters, treat upper and lower cases as the same
'''

#naive solution
def isPalindrome(string):
    # A man.' 
    string = ''.join(filter(str.isalnum,string)).lower() #remove non alpha numeric and convert to lower
    return ''.join(reversed(string)) == string
#time and space complexity O(n) 
 
#best solution - the pointer method

def isPalindrome_optimized(string):
    string = ''.join(filter(str.isalnum,string)).lower()
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left, right = left + 1, right - 1
    return True
#time complexity O(n), space: constant
