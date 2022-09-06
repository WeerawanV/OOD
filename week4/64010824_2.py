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

qES = Queue()
qEN = Queue()

for i in inp:
    temp = i.split(" ")
    if temp[0] == "ES":
        qES.enQueue(temp[1])

    elif temp[0] == "EN":
        qEN.enQueue(temp[1])

    elif temp[0] == "D":
        if qEN.isEmpty() and qES.isEmpty():
            print("Empty")
        elif qES.size() != 0:
            print(qES.deQueue())
        else:
            print(qEN.deQueue())