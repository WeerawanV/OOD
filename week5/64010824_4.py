'''กฤษฎาได้มีไอเดียสุดบรรเจิดคือการสร้างโปรแกรม Text Editor แบบ VIM ขึ้นมาใช้งานเอง โดยโปรแกรมนี้จะมีอยู่แค่ 1 Mode คือ Command Mode (inputของเรานั่นแหละ) โดยจะมีคำสั่งอยู่ 5 แบบ คือ 
Insert (I) , Left (L) , Right (R) , Backspace (B) และ Delete (D) (โดยความสามารถของคำสั่งต่างๆจะอธิบายด้านล่าง) แต่กฤษฎาไม่มีความสามารถทางด้านการสร้างโปรแกรมเลย 
กฤษฎาจึงได้มาขอร้องน้องๆที่เรียนอยู่วิศวกรรมคอมพิวเตอร์ ให้ช่วยสร้างโปรแกรม Text Editor ที่กฤษฎาต้องการให้หน่อย โดยผลลัพธ์ให้แสดงออกมาเป็น word ที่เหลืออยู่จาก Command ที่เราใส่ลงไป 
พร้อมกับตำแหน่งของ Cursor

***** อธิบาย Input 5 แบบ *****

1.  I <word > :   เป็นการนำ word ลงไปใส่ในตำแหน่งของ Cursor ปัจจุบัน หลังจากใส่ word เสร็จ ตำแหน่งของ Cursor จะมาอยู่ด้านหลังของ word ที่ใส่ลงไป
2.  L              :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านซ้าย 1 ตำแหน่ง หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร
3.  R             :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านขวา 1 ตำแหน่ง หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร
4.  B             :   เป็นการลบ word 1 ตัวทางด้านซ้ายของ Cursor หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร
5.  D             :   เป็นการลบ word 1 ตัวทางด้านขวาของ Cursor หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร '''

class LinkedList:

    class Node:
        def __init__(self,value):
            self.value = value
            self.next = None
            self.previous = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __str__(self):
        cur,s = self.head , str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
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

    def __len__ (self):
        p = self.head
        size = 0
        while p != None:
            size += 1
            p = p.next
        return size

    def insert(self,i,item):
        if len(self)==0:
            self.addHead(item)   
        else:
            if i<0:
                if(-i>len(self)):
                    i=-1
                else:
                    i=len(self)+i-1
            if i>=len(self):
                i=len(self)-1
            if i==-1:
                self.addHead(item)
            else:
                q = self.nodeAt(i)
                p = self.Node(item)
                if len(self)-1!=i:
                    r = self.nodeAt(i+1)
                    r.previous = p

                p.next = q.next
                q.next = p
                p.previous = q
                
                if i==len(self)-1:
                    self.tail = p
                self.size += 1
    
    def addHead(self, item):
        if self.head == None:
            p = self.Node(item)
            self.head = p
            self.tail = p
        else:
            t = self.Node(item)
            self.head.previous = t
            self.head.previous.next = self.head
            self.head = t

    def deleteAfter(self,p):
        p = self.head
        if len(self) > 0:
            p.next = p.next.next
            self.size -= 1

    def deleteHead(self):
        p = self.head.next
        p.previous = None
        self.head = p 
        self.size -= 1

    def nodeAt(self,i):
        p = self.head
        for j in range(0,i):
            p = p.next
        return p

inp = input("Enter Input : ").split(",")
nowCursor = 0
L = LinkedList()

for i in inp:
    if i[0] == "I": #insert word
        if nowCursor != 0:
            L.insert(nowCursor -1, i[2:]) 
        else:
            L.addHead(i[2:])
        nowCursor += 1

    elif i[0] == "L" and nowCursor > 0: #move left
        nowCursor -= 1

    elif i[0] == "R" and nowCursor < len(L): #move right
        nowCursor += 1

    elif i[0] == "B" and nowCursor > 0: #delete left
        nowCursor -= 1
        L.deleteAfter(nowCursor -1)

    elif i[0] == "D" and nowCursor < len(L): #delete right
        if nowCursor == 0:
            L.deleteHead()
        else:
            L.deleteAfter(nowCursor -1)

for i in range(len(L)):
    if i == nowCursor:
        print("|" , end=" ")
    print(L.nodeAt(i).value, end=" ")
if(nowCursor == len(L)):
    print("|" ,end=" ")
