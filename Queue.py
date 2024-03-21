from Node import Node

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    
    # checks if the queue is empty, consulting the first element 
    def is_empty(self):
        return self.first is None
    
    # returns the value of the first element if it is not none
    def peek(self):
        if not self.is_empty():
            return self.first.value
        None
    
    # add an element to the queue
    def push(self, value):
        new_node = Node(value)
        
        if self.last is None:
            self.last = self.first = new_node
            return
        
        self.last.next = new_node
        self.last = new_node
     
    # removes the first element from the queue and returns its value   
    def pop(self):
        if self.is_empty():
            return None
        
        removed_node = self.first
        self.first = self.first.next
        
        if self.first is None:
            self.last = None
            
        return removed_node.value
    