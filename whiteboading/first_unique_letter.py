'''
input: a string
output: the index of the first unique letter
'''

def unique_letter(string):
    if len(string) < 1:
        return -1
    elif len(string) == 1:
        return string
    else:
        letters = {}
        for ch in string:
            if ch not in letters:
                letters[ch] = 1
            else:
                letters[ch] += 1
        for i,ch in enumerate(s): #to get both the index and the value
            if letters[ch] == 1:
                return i
        return -1

#better py solution .index() and .rindex()
def unique_letter_method(string):
    for i, ch in enumerate(string):
        if string.index(ch) == string.rindex(ch): #.index is for the first apparence of the charachter and .rindex is for the last
            return i
    return -1

    