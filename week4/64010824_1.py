class Queue:

    def __init__ (self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def enQueue(self,i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

inp = input("Enter Input : ").split(",")

q = Queue()

for i in inp:
    temp = i.split(" ")
    if i[0] == "E":
        q.enQueue(temp[1])
        print(q.size())
    elif i == "D":
        if q.isEmpty():
            print("-1")
        else:
            print(q.items[0] ,"0")
            q.deQueue()
            
if q.isEmpty():
    print("Empty")
else:
    print(*q.items)
