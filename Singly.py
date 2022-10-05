# singly linked list : มี next อย่างเดียว

class node :
    def __init__(self,data) :       # สร้าง Node
        self.data = data            # ใส่ data ให้ node
        self.next = None            # ไว้เก็บ address ของ node ถัดไป

class linkedList :
    def __init__(self) :
        self.head = None            # node แรก ::  ตัวนี้คือ DUMMY NODE - node ที่เก็บค่า address ของ node แรกของ  linked list
        self.tail = None            # node สุดท้าย ( มีหรือไม่มีก็ได้ )
        self.linkedListSize = 0     # ให้เป็น linked list เปล่า ไม่มี node ใด ๆ  : size  เป็น 0

    def __str__(self) :             # ใช้กำหนดรูปแบบการแสดงผล : แก้ไขที่ s โดย ต้อง return เป็น string เท่านั้น
        s = ""
        now = self.head
        while now :
            s += str(now.data) + " "
            now = now.next
        s += "\nsize : " + str(self.linkedListSize)
        return s

    def isEmpty(self) :
        return self.linkedListSize == 0
        # หรือ  return self.head == None : ไม่มีสมาชิกเลย
    
    def append(self,item) :
        newNode = node(item)        # สร้าง node ของ item ที่ต้องการ
        if self.head is None :
            self.head = newNode     # ถ้า linked list ว่าง -> ให้ node นั้นเป็น head ( ตัวแรก ) ได้เลย
        else : 
            now = self.head         # iterator " now " ชี้ไปที่เดียวกับ iterator " head 
            while now.next :        # หรือ now.next != None : ให้ now หยุดที่ตัวสุดท้าย
                now = now.next
            now.next = newNode      # now คือ สุดท้าย -> now.next คือ หลัง node สุดท้าย -> ให้สุดท้าย = newNode
            # หรือ  self.tail.next = newNode 
        self.linkedListSize += 1    # เพิ่มตัวเก็บจำนวน node ใน linked list
        self.tail = newNode         # ให้ newNode คือตัวสุดท้าย
 
    def insert(self,pos,item) :
        newNode = node(item)
        if pos == 0 :
            newNode.next = self.head        # ให้ linked list เดิมไปต่อท้าย node ใหม่
            self.head = newNode             # ย้าย iterator " head " ไปชี้ที่ newNode
            self.linkedListSize += 1
        else :
            now = self.head
            for i in range(pos-1) :
                now = now.next              # ให้ iterator " now " หยุดที่ตัวที่ pos - 1 ( node : pos -2 ) เพื่อใส่ node ใหม่ต่อท้ายที่ pos พอดี
            
            if now :
                newNode.next = now.next     # ให้ตัวที่ pos ( node : pos - 1 ) ใน linked list เดิมไปต่อ newNode ( จะขยับตัวที่ pos ของ linked list เดิมไปเป็นตัวที่ pos + 1 ( node : pos ) ไปเรื่อย ๆ )
                now.next = newNode          # ใส่ newNode เป็น node ที่ pos
                self.linkedListSize += 1

    def popIndex(self,index) :
        now = self.head

        if index == 0 :
            self.head = now.next            # ขยับ iterator " head " ไป node ที่ 1 ( ตัวแรกเป็น node ที่ 0 )
            self.linkedListSize -= 1

        elif index == self.linkedListSize - 1 :     # ลบตัวสุดท้าย
            self.pop()

        else :

            for i in range (index-1) :              # ให้ iterator now หยุดที่ pos - 1
                now = now.next                      
                 
            cur = now.next.next                     # ให้ iterator cur ชี้ที่ pos + 1            
            now.next = cur                          # ให้ now มีตัวถัดไปเป็น cur ( จะข้ามตัวที่ pos ไป )
                
            self.linkedListSize -= 1

    def pop(self) :
        now = self.head 
        while now.next.next :                       # ให้ iterator " now " หยุดที่ตัว ' ก่อน ' สุดท้าย
            now = now.next
        self.tail = now                             # ขยับ iterator tail ให้เป็นตัวรองสุดท้าย : เพราะจะลบตัวสุดท้าย
        now.next = None                             # ให้ตัวสุดท้ายเป็น None
        self.linkedListSize -= 1

    def index(self,item) :
        i = 0                                       # ใช้เป็นตัวนับค่า index
        now = self.head
        while now :                                 # ดูถึงตัวสุดท้าย
            if now.data == item :
                return i                            # ถ้าข้อมูลใน node ที่ iterator now ชี้ไปเท่ากับ item ให้ return ค่า i
            i += 1                                  # ถ้ายังไม่เท่ากับ item ก็ขยับค่า index ไปเรื่อย ๆ
            now = now.next
        return -1                                   # ถ้าไม่เจออะไรเลยให้ return -1

    def search(self,item) :
        if self.index(item) == -1 :                 # ได้ผลลัพธ์จาก index(self)  ถ้าได้ -1 กลับมาคือไม่มีอยู่ใน linked list
            return False
        else :
            return True                            

# testing program

ll = linkedList()

ll.append(1)
ll.append(2)
ll.insert(0,0)
ll.insert(2,"insert1")
ll.popIndex(1)
ll.pop()

print(ll)
print(ll.search(3),ll.index(3))
print(ll.search(0),ll.index(0))
print(ll.head.data,ll.tail.data)