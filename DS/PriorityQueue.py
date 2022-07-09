


import heapq
class PriorityQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not self.items

    def put(self,priority,item):
        heapq.heappush(self.items,(priority,item))    #priority first then item that's the syntax

    def get(self):
        return heapq.heappop(self.items)[1]   #return the second element of the tuple

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)



if not '__main__':
    pass
else:
    pq=PriorityQueue()
    pq.put(2,"B")
    pq.put(1,"A")
    pq.put(3,"C")
    print(pq)
