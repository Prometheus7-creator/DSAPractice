class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

class LinkedListStack:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return True if self.head is None else False
    
    def push(self, val):
        new_node = Node(val)
        new_node.next_node = self.head
        self.head = new_node
    
    def pop(self):
        if self.isEmpty():
            return None
        popped = self.head.val
        self.head = self.head.next_node
        return popped
    
    def top(self):
        return None if self.isEmpty() else self.head.val

class ArrayStack:
    
    def __init__(self):
        self.array = []
        
    def isEmpty(self):
        return len(self.array)==0
    
    def push(self, val):
        self.array.append(val)
    
    def pop(self):
        return self.array.pop() if self.array else None
    
    def top(self):
        return self.array[-1] if self.array else None
