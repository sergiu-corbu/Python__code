#given a string of words, reverse all words

def reverse(s):
    #return " ".join(reversed(s.split()))
    s = s.split()
    s.reverse()
    return s

print(reverse("This is the best"))