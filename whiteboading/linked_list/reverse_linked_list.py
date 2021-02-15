

def reverseList(head):
    on = head
    prev = None
    while on:
        temp = on.next
        on.next = prev
        prev = on
        on = temp
    return prev

def reverseListR(on, prev = None):
    if on is None:
        return prev
    temp = on.next
    on.next = prev
    return reverseListR(temp, on)
