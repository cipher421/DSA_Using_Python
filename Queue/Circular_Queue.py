class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.items=[None]*size
        self.front=size.rear=-1

    def enqueue(self,value):
        # The next rear position is front when the circular queue is full.
        if ((self.rear + 1) == self.front):
            print("Queue is Full")
        elif self.front==-1:
            self.front=self.rear=0
            self.items[self.rear]=value
        else:
            # Wrap around to index 0 when the rear reaches the array end.
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
            # Move the front forward, wrapping around when necessary.
            self.front=(self.front+1)%self.size