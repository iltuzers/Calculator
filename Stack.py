class Stack:
    
    def __init__(self):
        self._items = [] # Use list to keep items in a Stack
    
    """ Add an item to the Stack """
    def push(self, item):
        self.items.append(item) # The top of stack is the end of list
    
    """ Return the top of Stack """
    def pop(self):
        return self.items.pop() # LAST IN FIRST OUT
    
    """ Check the top element of the Stack. It doesn't remove the item """
    def peek(self):
        return self.items[len(self.items) - 1]
    
    """ Check if the Stack is empty """
    def is_empty(self):
        return len(self.items) == 0
    
    """ Check the size of the Stack """
    def size(self):
        return len(self.items)