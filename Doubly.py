# Doubly Linked list : มี next กับ previous

class node :
    def __init__(self,data) :
        self.data = data
        self.next = None
        self.previous = None                        # ไว้เก็บ address ของ node ก่อนหน้า

class linkedList :
    def __init__(self) :
        self.head = None
        self.tail = None
        self.linkedListSize = 0

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

    def addHead(self,item) :
        newNode = node(item)
        if self.head is None :
            self.head = newNode
            self.tail = newNode             # ถ้า head ว่าง คือไม่มีสมาชิก -> newNode จะเป็นทั้ง head และ tail
        else :
            newNode.next = self.head        # นำ head ของ linked list มาต่อท้าย newNode 
            self.head.previous = newNode    # กำหนด node previous ของ head linked list เป็น newNode
            self.head = newNode             # ย้าย iterator " head " ของ linked list ไปที่ newNode
        self.linkedListSize += 1            # เพิ่มตัวเก็บจำนวน node ใน linked list

    def append(self,item) :
        newNode = node(item)
        if self.head is None :
            self.head = newNode 
        else :
            self.tail.next = newNode        # ให้ node ถัดจากตัวสุดท้ายของ linked list คือ newNode
            newNode.previous = self.tail    # ให้ newNode มีตัวก่อนหน้าเป็นตัวสุดท้ายของ linked list
        self.tail = newNode                 # ให้ newNode คือตัวสุดท้าย
        self.linkedListSize += 1

    def insert(self,pos,item) :
        if pos == 0 :                           # เพิ่มตัวแรก
            self.addHead(item)
        elif pos == self.linkedListSize -1 :    # เพิ่มตัวสุดท้าย
            self.append(item)
        else :
            newNode = node(item)
            now = self.head
            for i in range(pos-1) :
                now = now.next                  # ให้ iterator " now " หยุดที่ตัวที่ pos - 1 ( node : pos -2 ) เพื่อใส่ node ใหม่ต่อท้ายที่ pos พอดี
            cur = now.next                      # ให้ iterator " cur " เท้ากับตัวถัดจาก now : ตัวที่ pos ( node : pos - 1 )
            now.next = newNode                  # ให้ตัวถัดจาก node ที่ iterator " now " ชี้ ย้ายไปชี้ที่ newNode
            newNode.previous = now              # เชื่อมตัวก่อน newNode ให้เป็น node ที่ iterator " now " ชี้
            newNode.next = cur                  # เชื่อมตัวถัดจาก newNode ให้เป็น node ที่ iterator " cur " ชี้
            cur.previous = newNode              # เชื่อมตัวก่อน iterator " cur " ชี้ ให้เป็น newNode
            self.linkedListSize += 1

    def pop(self) :
        now = self.tail.previous                # ให้ iterator " now " ชี้ที่ตัว ' ก่อน ' สุดท้าย
        self.tail = now                         # ให้ iterator " tail " ชี้ที่ตัว ' ก่อน ' สุดท้ายที่ iterator " now " ชี้
        now.next = None                         # ให้ node ถัดจากที่ iterator " now " ชี้ ( ตัวสุดท้ายเดิม ) เป็น None
        self.linkedListSize -= 1

    def popIndex(self,index) :
        if index == 0 :
            self.head = self.head.next              # ย้าย iterator " head " ของ linked list ไปที่ตัวถัดไป ( node : 1 )
            self.head.previous = None               # เปลี่ยน head เดิม ( ตัว previous ของ head ปัจจุบัน ) เป็น None
            self.linkedListSize -= 1
        elif index == self.linkedListSize - 1 :     # ลบตัวสุดท้าย
            self.pop()
        else :
            now = self.head
            for i in range(index-1) :
                now = now.next                      # ให้ iterator now หยุดที่ pos - 1
            cur = now.next.next                     # ให้ iterator cur ชี้ที่ pos + 1
            now.next = cur                          # ให้ node ทีี่ iterator " now " ชี้มี node ถัดไปเป็น node ทีี่ iterator " cur " ชี้
            cur.previous = now                      # ให้ node ทีี่ iterator " cur " ชี้มี node ก่อนหน้าเป็น node ทีี่ iterator " now " ชี้
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
ll.insert(2,3)
ll.insert(1,"insert1")
ll.pop()
ll.popIndex(0)
ll.popIndex(1)

print(ll)