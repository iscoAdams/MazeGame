import sys
import os
"""
for line in read_file:
            listItems = line.split()
            mapObject = map(int, listItems)
            print(*mapObject)
            for item in mapObject:
                s.push(item)
#i used this function to get the input from the file dinamically
stackList = [::-1] this use to reverse the list
stackList = [:-1] all but the last
stackList = [1:] all but the first
"""

class Stack:
    def __init__(self): #constructor and as i see it doesn't expect any input so i just can call it as a nurmal function and when i import it i can just prefix the name of the file and then the name of the class
        self.items = []

    def isEmpty(self):
        return not self.items   # self.items == []   # return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if(self.isEmpty()):
            return None
        return self.items.pop()

    def peek(self): # return self.items[len(self.items)-1]
        if(self.isEmpty()):
            return None
        return self.items[-1] 

    def size(self):
        return len(self.items)
           
    def __str__(self): #for parsing the output and not getting the stack object or non meaningful output 
        return str(self.items)       



if not '__main__': # if not main file that i excute right now pass else then do something
    pass