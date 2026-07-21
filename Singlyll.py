class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlylinkedlist:
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
        else:
            newnode.next=self.head
            self.head=newnode
    def insertEnd(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newnode
    def search(self,target):
        if self.head is None:
            print("sll is empty")
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
            print("sll is empty")
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            del temp
    def delEnd(self):
        if self.head is None:
            print("sll is empty")
        else:
            temp=self.head
            while temp.next.next:
                temp=temp.next
            delnode=temp.next
            temp.next=None
            del delnode

sll=singlylinkedlist()
sll.insertBegin(120)
sll.insertBegin(30)
sll.insertBegin(100)
sll.insertBegin(110)
sll.insertBegin(200)
sll.display()
print()
sll.insertEnd(10)
sll.insertEnd(20)
sll.display()
print()
sll.search(30)
sll.search(1)
sll.display()
print()
sll.delBegin()
sll.display()
print()
sll.delEnd()
sll.display()
print()
