class TwoStacks:
    
    def __init__(self, capacity):
        
        self.array = [None for _ in range(capacity)]
        
        self.stack1, self.stack2 = -1,capacity
        
        self.capacity = capacity
        
    def push1(self,val):
        
        if self.stack2 - self.stack1 > 1:
            
            self.stack1 += 1
            
            self.array[self.stack1] = val
        
        else:
            
            print("Stack overflow")
    
    def push2(self,val):
        
        if self.stack2 - self.stack1 > 1:
            
            self.stack2 -= 1
            
            self.array[self.stack2] = val
            
        else:
            
            print("Stack overflow")
    
    def pop1(self):
        
        if self.stack1 >= 0:
            
            x = self.array[self.stack1]
            
            self.stack1 -= 1
            
            return x
        
        else:
            
            print("Stack underflow")
            
            return None
    
    def pop2(self):
        
        if self.stack2 < self.capacity:
            
            x = self.array[self.stack2]
            
            self.stack2 += 1
            
            return x
        
        else:
            
            print("Stack underflow")
            
            return None
