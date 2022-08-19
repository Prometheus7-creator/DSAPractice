class Queue:
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, val):
        self.stack1.append(val)
    
    def dequeue(self):
        if not (self.stack1 or self.stack2): return None
        if not self.stack2 and self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()
