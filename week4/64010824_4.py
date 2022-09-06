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

    def returnQueue(self):
        return self.items

    def insertQueue(self,i,mark):
        self.temp = []
        for e in range(mark):
            self.temp.append(self.items[e])
        self.temp.append(i)
        for e in range (mark,len(self.items)):
            self.temp.append(self.items[e])
        self.items = self.temp

id,inp = input("Enter Input : ").split("/")
id = list(id.split(","))
inp = list(inp.split(","))

q1 = Queue() #id
q2 = Queue() #inp

for i in inp:
    temp = i.split()
    if temp[0] == "D":
        if q1.size() == 0:
            print("Empty")
        else:
            print(q1.deQueue())
            q2.deQueue()
    elif temp[0] == "E":
        for e in id:
            temp2 = e.split()
            if temp2[1] == temp[1]:
                mark = q1.size()
                for ID in range(q2.size()-1,-1,-1):
                    if q2.returnQueue()[ID] == temp2[0]:
                        mark = ID+1
                        break
                if mark == q1.size():
                    q1.enQueue(temp2[1])
                    q2.enQueue(temp2[0])
                else:
                    q1.insertQueue(temp2[1],mark)
                    q2.insertQueue(temp2[0],mark)
