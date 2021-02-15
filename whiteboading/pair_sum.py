''' 
pair_sum function: ([numbers], value)
print pairs of 2 numbers added together equals value
([1,3,2,2],4) -> {(1,3),(2,2)}
'''

def pair_sum(array, value):
    if len(array) < 2:
        return print("The array is unusable. Please insert at least 2 numbers")
    
    seen = set()
    output = set()

    for num in array:
        target = value - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target),max(num, target)))
    print('\n'.join(map(str, list(output))))

pair_sum([1,3,2,2],4)


