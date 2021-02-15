#deque function
from collections import deque
'''
queue = deque()
queue.append(5)
queue.append(10)
print(queue)
print(queue.popleft())
'''
#usual class

class Queue():
    def __init__(self):
        self.queue = deque()
        self.size = 0
    def enqueue(self, item):
        self.queue.append(item)
        self.size += 1
    def dequeue(self, item):
        if self.size > 0:
            self.size -=1
            return self.queue.popleft()
        else:
            return None
    def peek(self):
        if self.size > 0:
            val = self.queue.popleft()
            queue.appendleft(val)
            return val
        else:
            return None
    def get_size(self):
        return self.size
        