'''
input: an array of strings
output: an array of arrays of strings
edge cases: empty array
time complexity: O(n*(mlogm))
space complexity; O(n)
sorted() time complexity: nlogn
'''

def group_anagrams(strings):
    ht = {}
    for string in strings:
        sorted_string = ''.join(sorted(string)) #otherwise we ll get a string of strings for each letter
        if sorted_string in ht:
            ht[sorted_string].append(string)
        else:
            ht[sorted_string] = [string]
    return ht.values()

lst = ["ab","ba","bb","bba"]
print(group_anagrams(lst))