class Queue:
    def __init__(self):
        self.qu=[]
    def isEmpty(self):
        if self.qu==[]:
            return True
        else:
            return False
    def enqueue(self,x):
        self.qu.append(x)
    def dequeue(self):
        if self.isEmpty():
            return -1
        else:
            popped=self.qu.pop(0)
            return popped
    def peek(self):
        if self.isEmpty():
            return -1
        else:
            return self.qu[0]
    def display(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            for i in range(len(self.qu)):
                print(self.qu[i])
                print('______')
            print()
    def search(self,target):
        if self.isEmpty():
            print("queue is empty")
        else:
            for i in range(len(self.qu)):
                if self.qu[i]==target:
                    print("found")
                    break
            else:
                    print("not found")

q1=Queue()
while True:
    print('_____operations_____')
    print('1.enqueue')
    print('2.dequeue')
    print('3.peek')
    print('4.display')
    print('5.search')
    print('6.exit')
    option=int(input("enter operation"))
    if option==1:
        ele=int(input("enter ele: "))
        q1.enqueue(ele)
    elif option==2:
        res=q1.dequeue()
        if res !=-1:
            print(f'popped: {res}')
        else:
            print("underflow")
    elif option==3:
        res=q1.peek()
        if res==-1:
            print("underflow")
        else:
            print(f'top ele is: {res}')
    elif option==4:
        q1.display()
    elif option==5:
        target=int(input("search for: "))
        q1.search(target)
    elif option==6:
        break
    else:
        print("enter valid option")
        
                
        
