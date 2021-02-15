class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None #initialize the pointer

node = ListNode(1)
node.next = ListNode(2)
head = ListNode(0)
head.next = node 

#looping over a linked list

on = head
while on!= None:
    print(on.value)
    on = on.next