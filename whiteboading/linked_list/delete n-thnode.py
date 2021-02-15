'''
traversal and change of pointer
and return the head
edge cases: last node(n=0)
            first node(n=length-1)
assumptions:at least one node
'''

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeNthfromEnd(head, n):
    #measure the length, point around node n, handle head deletion
    on = head
    length = 1
    while on != None:
        on = on.next
        length += 1
    left_index = length - n - 1
    if left_index == 0:
        return head.next
    on = head
    while left_index >1:
        on = on.next
        left_index -= 1
    on.next = on.next.next
    return head

