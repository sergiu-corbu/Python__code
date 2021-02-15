
def bubble_sort(lst):
    for i in range(0,len(lst)-1):
        for j in range(0, len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def insertion_sort(lst):
    #not recommended for large data sets, O(n2) complexity
    for i in range(1,len(lst)):
        current_num = lst[i]
        for j in range(i-1,0,-1):
            if lst[j] > current_num:
                lst[j+1] = lst[j]
            else:
                lst[j+1] = current_num
                break
    return lst


def merge_sort(lst):
    #recursive algorithm(divide and conquer), best for large data sets,  complexity O(nlogn)
    position(lst,0,len(lst)-1)

def position(lst,first,last):
    if first < last:
        middle = (first + last)//2
        position(lst,first,middle)
        position(lst,middle+1,last)
        merge(lst,first,middle,last)

def merge(lst, first,middle,last):
    l = lst[first:middle]
    r = lst[middle:last+1]
    l.append(99999999)
    r.append(99999999)
    i = j = 0
    for k in range(first, last+1):
        if l[i] <= r[j]:
            lst[k] = l[i]
            i += 1
        else:
            lst[k] = r[j]
            j += 1

#alist = ['b', 'd', 'f', 'a', 'c', 'e']
alist1 = [12,5,15,166,90,3]
print(merge_sort(alist1))