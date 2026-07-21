class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class doublylinkedlist:
    def __init__(self):
        self.head=None
        self.next=None
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp =temp.next
    def insertBegin(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
    def insertEnd(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.prev=self.tail
            self.tail.next=newnode
            self.tail=newnode
    def search(self,target):
        if self.head is None:
            print("Dll is empty")
        else:
            temp=self.head
            while temp:
                if temp.data==target:
                    print("found")
                    break
                else:
                    temp=temp.next
            else:
                print("not found")
    def delBegin(self):
        if self.head is None:
            print("Dll is empty")
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            self.head.prev=None
            del temp
    def delEnd(self):
        if self.head is None:
            print("Dll is empty")
        else:
            temp=self.tail
            self.tail=self.tail.prev
            temp.prev=None
            self.tail.next=None
            del temp
    def display(self):
        if self.head is None:
            print("Dll is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=' ')
                temp=temp.next
                
            

Dll=doublylinkedlist()
Dll.insertBegin(120)
Dll.insertBegin(30)
Dll.insertBegin(100)
Dll.insertBegin(110)
Dll.insertBegin(200)
Dll.display()
print()
Dll.insertEnd(10)
Dll.insertEnd(20)
Dll.display()
print()
Dll.search(12)
Dll.search(30)
Dll.display()
print()
Dll.delBegin()
Dll.display()
print()
Dll.delEnd()
Dll.display()
print()
