class stack(list):
    def __init__(self):
        list.__init__(self)
    
    def pop(self):
        return super().pop()
    
    def push(self,item):
        self.append(item)
        
    def is_empty(self):
        return len(self)==0
    
    def peek(self):
        if not self.is_empty():
           temp=super().pop()
           self.append(temp)
           return temp

    def get_siez(self):
        return len(self)
    


    