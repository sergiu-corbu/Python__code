def p_t(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            for k in range(j+1, len(list)):
                if list[i]**2 + list[j]**2 == list[k]**2:
                    return True
    return False
lst = [1,3,4,2,5,6,7]
print(p_t(lst))

