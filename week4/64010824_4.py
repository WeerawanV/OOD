''' โรงอาหารของบริษัทแห่งหนึ่ง จะมีเจ้าหน้าที่คอยจัดแถวสำหรับการซื้ออาหาร โดยจะมีหลักการคือจะดูจากแผนกของพนักงานแต่ละคนว่าอยู่แผนกไหน ถ้าหากในแถวที่ต่ออยู่มีแผนกนั้น 
จะนำพนักงานคนนั้นแทรกไปด้านหลังของแผนกเดียวกัน ตัวอย่างเช่น
Front | 1 2 2 2 2 3 3 3 | Rear  จาก Queue ถ้าหากมีพนักงานแผนก1เข้ามา Queue จะกลายเป็น Front | 1 1 2 2 2 2 3 3 3 | Rear

Input :
จะแบ่งเป็น 2 ฝั่งแบ่งด้วย / คือ ซ้าย : เป็นแผนกของพนักงานและIDของพนักงานแต่ละคน  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
E < id >  ->  เป็นการนำพนักงานเข้า Queue
D  ->  เป็นการนำพนักงานคนหน้าสุดออกจากแถว โดยจะแสดงผลเป็น id ของพนักงานคนนั้น ถ้าหากไม่มีพนักงานในแถวจะทำการแสดงผลเป็น Empty

อธิบาย TestCase_1 :  จะมีพนักงาน 4 คน คือแผนก 1 id=101,102 และแผนก 2 id=201,202  ต่อมาจะแสดงผล Empty เพราะยังไม่มีพนักงานในแถว  
และนำพนักงาน id=101และ201 เข้าแถวตามลำดับ ต่อมาจะแสดงผลเป็น 101 เพราะพนักงาน 101 อยู่คนแรกและแสดงผล 201 เพราะอยู่คนแรก '''

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
