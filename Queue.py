""" FIFO : First In First Out"""
class Queue:

    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item) # The Rear of the queue is at the position 0 of the list
    
    def dequeue(self):
        self.items.pop() # The Front of the queue is the last element of the list
    
    def peek(self):
        if not self.is_empty():
            return self.items[len(self.items) - 1]
        else:
            raise IndexError("Empty Queue")
    
    def is_empty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.items)
        
