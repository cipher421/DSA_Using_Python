class dequeue:
    def __init__(self):
        self.item=[]

    def isEmpty(self):
        return len(self.item)==0

    def insertAtEnd(self,value):
        # A deque allows insertion at either end.
        self.item.append(value)

    def deleteAtFront(self):
        if (self.isEmpty()):
            raise Exception("Queue is empty")
        else:
            # Remove the oldest value from the front.
            return self.item.pop(0)

    def InsertAtFront(self,value):
        self.item.insert(0,value)

    def deleteAtEnd(self):
        if (self.isEmpty()):
            raise Exception("Queue is empty")
        else:
            # Remove the newest value from the back.
            return self.item.pop()

q=dequeue()
q.insertAtEnd(10)
q.InsertAtFront(20)
q.insertAtEnd(30)
q.InsertAtFront(40)

print(q.deleteAtEnd())
print(q.deleteAtEnd())
print(q.deleteAtFront())
print(q.deleteAtFront())
print(q.deleteAtEnd())
print(q.deleteAtFront())