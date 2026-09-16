class Queue:
    def __init__(self):
        self.item=[]

    def isEmpty(self):
        return len(self.item)==0

    def insert(self,value):
        self.item.append(value)

    def pop(self):
        if (self.isEmpty()):
            raise Exception("Queue is empty")
        else:
            return self.item.pop(0)


q=Queue()
q.insert(10)
q.insert(20)
q.insert(30)
q.insert(40)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())