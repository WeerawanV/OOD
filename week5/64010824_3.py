class LinkedList:
    
    class Node:
        def __init__(self,value):
            self.value = value
            self.next = None
            self.previous = None

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__ (self):
        cur,s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        cur,s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def append(self,item):
        if self.head == None:
            p = self.Node(item)
            self.head = p
            self.tail = p
        else:
            p = self.Node(item)
            q = self.tail
            q.next = p
            p.previous = self.tail
            self.tail = p

inp1,inp2 = input("Enter Input (L1,L2) : ").split()

s1 = str(inp1).split("->")
s2 = str(inp2).split("->")

L1 = LinkedList()
L2 = LinkedList()

for i in s1:
    L1.append(i)
print("L1    : " ,end="")
print(L1)

for i in s2:
    L2.append(i)
print("L2    : " ,end="")
print(L2)

print("Merge : " ,end="")
print(str(L1) + str(L2.reverse()))      