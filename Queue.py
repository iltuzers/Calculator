
class Queue:
""" FIFO : First In First Out"""
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """ Add an item to the Queue
        :param item: item to be added to the Queue
        :type item: str
        :rtype: None
        :return: It doesn't return anything
        
        """
        self.items.insert(0, item) # The Rear of the queue is at the position 0 of the list
    
    def dequeue(self):
         """ Remove and return the front of the Queue
        :rtype: str
        :return: the front of the Queue
        """
        try:
            return self.items.pop() # The Front of the queue is the last element of the list
        except IndexError:
            print("Empty Queue")
    
    def peek(self):
        """ Check the front element of the Queue. It doesn't remove the item
         :rtype: str
         :return: the front of the Queue
          """
        try:
            return self.items[len(self.items) - 1]
        except IndexError:
            print("Empty Queue")
            
    def is_empty(self):
        """ Check if the Queue is empty
         :rtype: bool
         :return: True or Falsee
         """
        return self.size() == 0
    
    def size(self):
        """ Check the size of the Queue
         :rtype: int
         :return: The length of the Queue
          """
        return len(self.items)
        
