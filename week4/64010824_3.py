#กลับมาอ่านเองด้วย!!!

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

book,inp = input("Enter Input : ").split("/")
book = list(book.split())
inp = list(inp.split(","))

q1 = Queue()
q2 = Queue()

for n in book:
    book_id = n.split()
    q1.enQueue(n)

for e in inp:
    temp = e.split()
    if temp[0] == "D":
        q1.deQueue()
    elif temp[0] == "E":
        q1.enQueue(temp[1])

r = q1.items
temp1 = []
i = 0
while i < q1.size():
    temp1.append(r.count(r[i]))
    i += 1

temp2 = dict(zip(r,temp1))
mode_list={i for (i,j) in temp2.items() if j == max(temp1) }

if len(mode_list)>1:
    print("NO Duplicate")
else:
    print("Duplicate")