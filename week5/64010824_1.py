class LinkedList:
    
    class Node:
        def __init__(self,data,next = None):
            self.data = data
            if next is None:
                self.next = None
            else:
                self.next = next
        
    def __init__(self):
        self.head = self.Node(None,None)
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return "List is empty"
        else:
            s = "link list : "
            p = self.head.next
            while p != None:
                s += str(p.data) 
                if p.next != None:
                    s += "->"
                p = p.next
            return s

    def __len__ (self):
        return self.size
   
    def isEmpty(self):
        return self.size == 0

    def nodeAt(self,i):
        p = self.head
        for j in range(-1,i):
            p = p.next
        return p

    def sizeOf(self):
        size = 0
        p = self.head.next
        while p != None:
            size += 1 
            p = p.next
        if self.isEmpty():
            size = 0
        return size

    def append(self,data):
        if self.head == None:
            p = self.Node(data)
            self.head = p
            self.size += 1
        else:
            self.insert(len(self),data)

    def insert(self,index,data):
        p = self.nodeAt(index-1)
        p.next = self.Node(data,p.next)
        self.size += 1
        
inp = input("Enter Input : ").split(",")

L = LinkedList()
set = False

for i in range(len(inp)):
    if i == 0:
        if inp[0] == "":
            set = True
        else:
            for e in inp[i].split(" "):
                L.append(e)
        if inp[0] == "":
            print("List is empty")
        else:
            print(L)
        continue
    
    index,data = inp[i].split(":")
    index = index.replace(" ",'')
    
    if int(index) >= 0 and int(data) <= L.sizeOf():
        index,data = inp[i].split(":")
        index = index.replace(" ",'')
        print("index = " + index + " and data = " + data)
        L.insert(int(index),int(data))
        if not L.isEmpty():
            print(L)
    else:
        print("Data cannot be added")
        if not L.isEmpty():
            print(L)
    if L.isEmpty():
        print("List is empty")
