''' Color rush 2 '''

class Queue:
    
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def enQueue(self,i):
        self.items.append(i)
    
    def deQueue(self):
        return self.items.pop(0)
    
    def deEndQueue(self):
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def returnQueue(self):
        return self.items

def checkPop(ls):
    q = Queue()
    List = ls
    List.reverse()
    indx = 2
    num = 0
    while indx < len(List):
        if List[indx] == List[indx-1] and List[indx-1] == List[indx-2]:
            q.enQueue(List[indx])
            List.pop(indx-2)
            List.pop(indx-2)
            List.pop(indx-2)
            indx = 2
            num += 1
        else:
            indx += 1
    q.enQueue(num)
    return q

def returnAfterPop(ls):
    q = Queue()
    List = ls
    List.reverse()
    indx = 2
    num = 0
    while indx < len(List):
        if List[indx] == List[indx-1] and List[indx-1] == List[indx-2]:
            List.pop(indx-2)
            List.pop(indx-2)
            List.pop(indx-2)
            indx = 2
            num += 1
        else:
            indx += 1
    for i in List:
        q.enQueue(i)
    q.enQueue(num)
    return q

normal = []
mirror = []
newNormal = []
nm,mr = input("Enter Input (Normal, Mirror) : ").split()

for i in range(len(nm)):
    normal.append(nm[i])

for j in range(len(mr)):
    mirror.append(mr[j])

q = checkPop(mirror)
ansMr = returnAfterPop(mirror)
ansMr.deEndQueue()
numExMr = q.deEndQueue()
num = 0
failed = 0
temp = normal[0]

for i in normal:
    if i==temp :
        num += 1
    else :
        temp = i
        num = 1
    if num==3 and q.size()!=0:
        kept = q.deQueue()
        if i==kept:
            failed += 1
        newNormal.append(kept)
        num = 0
    elif num==3:
        num = 0
    newNormal.append(i)

ans = returnAfterPop(newNormal)
numExNm = ans.deEndQueue()
print("NORMAL :")
print(ans.size())

if(ans.size()!=0):
    for i in ans.returnQueue():
        print(i,end="")
    print("")
else:
    print("Empty")
print(str(numExNm-failed)+" Explosive(s) ! ! ! (NORMAL)")

if failed != 0:
    print("Failed Interrupted "+str(failed)+" Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
print(ansMr.size())

if(ansMr.size()!=0):
    for i in ansMr.returnQueue():
        print(i,end="")
    print("")
else:
    print("ytpmE")
print("(RORRIM) ! ! ! (s)evisolpxE "+str(numExMr))
