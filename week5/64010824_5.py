'''ให้น้องๆใช้ Linked List (เขียนเป็น class)  ในการทำ Radix Sort  (มีอยู่ในสไลด์เรียน 2 หน้าสุดท้าย)  ในรูปแบบมากไปน้อย

โดยผลลัพธ์ให้ออกมาเป็นการทำ Radix Sort แบบจำนวนรอบน้อยที่สุด และแสดงผลในแต่ละรอบว่าได้ผลลัพธ์เป็นอย่างไร  3 บรรทัดสุดท้ายจะเป็น 
( จำนวนรอบที่น้อยที่สุด , Data ก่อนทำ Radix Sort และ Data หลังทำ Radix Sort ) '''

class LinkedList:

    class Node:
        def __init__(self,value):
            self.value = value
            self.next = None
            self.previous = None

    def __init__(self,max):
        self.head = None
        self.tail = None
        self.max = max
        self.count = 0
        self.max_length = 1

    def __str__(self):
        s = ""
        cur = self.tail
        while cur != None:
            s += str(cur.value) + " -> "
            cur = cur.next
        return s[:-3]

    def __len__ (self):
        return self.size
    
    def isEmpty(self):
        return self.head == None

    def nodeAt(self,i) :          
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p

    def length(self):
        return self.count

    def push(self,value):
        node = self.Node(value)
        if int(value) > 0:
            self.max_length = max(self.max_length, len(value))
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.head.next, node.previous = node, self.head
            self.head = node
        self.count += 1

    def push_front(self, value):
        node = self.Node(value)
        if int(value) > 0:
            self.max_length = max(self.max_length, len(value))
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.previous, node.next = node, self.tail
            self.tail = node
        self.count+=1

    def push_back(self, value):
        node = self.Node(value)
        if int(value) > 0:
            self.max_length = max(self.max_length, len(value))
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.next, node.previous = node, self.head
            self.head = node
        self.count+=1

    def pop_front(self):
        temp = self.tail.value
        try:
            self.tail = self.tail.next
            self.tail.previous = None  
            self.count-=1
        except:
            self.head = None
            self.tail = None
            self.count = 0
        return temp

    def sort(self):
        temp = []
        if not self.isEmpty():
            while not self.isEmpty():
                temp.append(int(self.pop_front()))
            for x in sorted(temp):
                self.push_front(str(x))

    def get_report(self):
        temp = ''
        current = self.tail
        while current:
            temp += str(current.value) + ' '
            current = current.next
        return temp

    def redix_sort(self):
        box = []
        for i in range(10):
            box.append(LinkedList(0))
        print("------------------------------------------------------------")
        stop = False
        counter = 0
        for i in range(self.max_length+1):
            print("Round : " + str(i+1))
            while not self.isEmpty():
                temp = self.pop_front()[::-1]
                try:
                    box[int(temp[i])].push_front(temp[::-1])   
                except:
                    box[0].push_front(temp[::-1])
            if box[0].length() == self.max:
                stop = True
            for j in range(10):
                box[j].sort()
                print(str(j) + ' : ' + box[j].get_report())
                while not box[j].isEmpty():
                    temp = box[j].pop_front()
                    self.push_back(temp)
            print("------------------------------------------------------------")
            counter += 1
            if stop:
                break
        self.max_length = counter

    def get_max_length(self):
        return str(self.max_length-1)

inp = input("Enter Input : ").split()

L = LinkedList(len(inp))
L2 = LinkedList(len(inp))
for x in inp:
    L2.push(x)
    L.push(x)

L2.redix_sort()
print(L2.get_max_length() + ' Time(s)')
print('Before Radix Sort : ' + str(L))
print('After  Radix Sort : ' + str(L2))
