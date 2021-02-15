def anagram1(s1,s2):
    s1.replace(' ','').lower()
    s2.replace(' ','').lower()

    if sorted(s1) != sorted(s2):
        return False
    return True

def anagram2(s1,s2):
    if len(s1) != len(s2):
        return False
    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            if letter not in count:
                count[letter] = 1
    for letter in s2:
        if letter in count:
            count[letter] -=1
        else:
            if letter not in count:
                count[letter] = 1
    for i in count:
        if count[i] != 0:
            return False
    return True
    
validate = anagram2("anab","baam")
print(validate)