'''
the stack method
determine if the input string is valid
edge cases: empty string -> return true
assumptions: no weird chaachters, so the input will be clean
close the most recent opened pharanthese
'''

def isValid(string):
    stack = []
    pairs = {
        '(': ')', '{': '}', '[':']'
    }
    for char in string:
        if char == '(' or char =='[' or char =='{':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            last = stack.pop()
            if pairs[last] != char:
                return False
    if len(stack) > 0:
        return False
    else: 
        return True
#linear time complexity, space: O(n)


string = "{[([])]]}"
print(isValid(string)) # -> false