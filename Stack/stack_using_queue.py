from collections import deque

class Stack:
    
    def __init__(self):
        
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, val):
        
        while self.q1:
            
            self.q2.append(self.q1.popleft())
        
        self.q1.append(val)
        
        while self.q2:
            
            self.q1.append(self.q2.popleft())
        
    
    def pop(self):
        
        return self.q1.popleft() if self.q1 else None
        
    
    def top(self):
        
        return self.q1[0] if self.q1 else None
