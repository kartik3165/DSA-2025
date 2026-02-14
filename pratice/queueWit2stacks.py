
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqeue(self,data):
        self.s1.append(data)

    def deqeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()
    
