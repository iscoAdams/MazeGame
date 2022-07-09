
#there is a module called queue in python so i can't name it queue
#and i want to avoid any confusion with the queue module
#list are not effiecient for this purpose as pending or removing items from the beginning of the list is expensive
#and i need to shift all by one
#so i will use a built in deque which is a double ended queue to emplement a queue
from collections import deque 
class Queue:
    def __init__(self):
        self.items = deque()
    def isEmpty(self):
        return not self.items
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.isEmpty():
            return None
        return self.items.popleft()  
    def peek(self):
        if self.isEmpty():
            return None
        return self.items[0]          

    def size(self):
        return len(self.items)

    def __str__(self): # give us human readeble of what is inside our object
        return str(self.items)


if not '__main__':
    pass
