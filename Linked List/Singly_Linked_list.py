class Node:
    def __init__(self, data,next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self,head=None):
        self.head=head

    def insertAtEnd(self,data):
        temp=Node(data)
        if(self.head!=None):
            # Walk to the final node and attach the new node after it.
            t1=self.head
            while(t1.next!=None):
                t1=t1.next
            t1.next=temp
        else:
            self.head=temp

    def insertAtBegin(self,data):
        temp=Node(data)
        # The new node becomes the head and points to the old head.
        temp.next=self.head
        self.head=temp

    def insertAtmiddle(self,data,pos):
        t1=self.head
        temp=Node(data)
        # Insert after the first node whose data matches the requested position.
        while(t1.next!=None):
            if(t1.data==pos):
                temp.next=t1.next
                t1.next=temp
            t1=t1.next

    def printLL(self):
        t1=self.head
        # Follow next references until the end of the linked list.
        while(t1.next!=None):
            print(t1.data,end="->")
            t1=t1.next
        if t1:
            print(t1.data)

    def delete(self,data):
        t1=self.head
        prev=t1
        # Link around the matching node so it is removed from the chain.
        if(t1.data==data):
            self.head=t1.next
        while(t1.next!=None):
            if(t1.data==data):
                prev.next=t1.next
                break
            else:
                prev=t1
                t1=t1.next
        if(t1.data==data):
            prev.next=None

ll=SinglyLinkedList()
ll.insertAtEnd(1)
ll.insertAtEnd(2)
ll.insertAtEnd(3)
ll.insertAtEnd(4)

ll.insertAtBegin(5)
ll.insertAtBegin(6)

ll.insertAtmiddle(7,2)
ll.insertAtmiddle(8,5)

ll.delete(6)
ll.delete(4)

ll.printLL()