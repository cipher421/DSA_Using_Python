class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.items=[None]*size
        self.front=size.rear=-1

    def enqueue(self,value):
        if ((self.rear + 1) == self.front):
            print("Queue is Full")
        elif self.front==-1:
            self.front=self.rear=0
            self.items[self.rear]=value
        else:
            self.rear=(self.rear+1)%self.size
            self.items[self.rear]=value

    def dequeue(self):
        if(self.front==-1):
            print("Queue is Empty")
        elif(self.front==self.rear):
            print(self.items[self.front])
            self.front=self.rear=-1
        else:
            print(self.items[self.front])
            self.front=(self.front+1)%self.size