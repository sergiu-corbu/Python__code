#find the maximum sum from an array containing positive and negative numbers

def largest_sum(array):
    if len(array) == 0:
        return print("The array is too small")
    max_sum = current_sum = array[0]

    for num in array[1:]: #first element is skipped
        current_sum = max(current_sum+num,num)
        max_sum = max(current_sum, max_sum)
    return max_sum

print(largest_sum([7,1,2,-1,3,4,10,-12,3,21,-19]))

