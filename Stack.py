class Stack:
    """ LIFO : Last In First Out"""
    def __init__(self):
        self.items = [] # Use list to keep items in a Stack
    
    
    def push(self, item):
        """ Add an item to the Stack
        :param item: item to be added to the Stack
        :type item: str
        :rtype: None
        :return: It doesn't return anything
        
        """
        self.items.append(item) # The top of stack is the end of list
    
    
    def pop(self):
        """ Remove and return the top of the Stack 
        :rtype: str
        :return: the top of the Stack
        
        """
        try :
            return self.items.pop() # LAST IN FIRST OUT
        except IndexError:
            print("Empty Stack")
    
   
    def peek(self):
         """ Check the top element of the Stack. It doesn't remove the item
         :rtype: str
         :return: the top of the Stack
          """
        try:
            return self.items[len(self.items) - 1]
        except IndexError:
            print("Stack is Empty")
       
    
    def is_empty(self):
        """ Check if the Stack is empty
         :rtype: bool
         :return: True or Falsee
         """
        return len(self.items) == 0
    
   
    def size(self):
         """ Check the size of the Stack
         :rtype: int
         :return: The length of the Stack
          """
        return len(self.items)