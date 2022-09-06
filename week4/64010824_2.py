'''PSD48 (P-Saderd 48 Group) เป็นวงไอดอลวงหนึ่งที่กระแสกำลังมาแรง ณ ตอนนี้โดยเพลงที่ได้รับความนิยมอย่างมากคือเพลงจี่หอย โดยวง PSD48 กำลังจะจัดงานจับมือขึ้น 
โดยมีกฎอยู่ว่าถ้าหากคนที่กำลังต่อแถวอยู่เป็นคนจาก กองกำลังสำรวจ จะได้สิทธิพิเศษในการแทรกแถวไปข้างหน้าสุดทันที (แต่ถ้าหากคนหน้าสุดก็เป็นคนของกองกำลังสำรวจก็ต้องต่อหลังเขาอยู่ดี)  
PSD48 อยากให้คุณช่วยเขียนโปรแกรมสำหรับหาว่าจะมีโอตะ id ใดบ้างที่ได้จับมือ

Input :
EN <value>  เป็นโอตะธรรมดา  id = value
ES <value>  เป็นโอตะของกองกำลังสำรวจ  id = value
D           เป็นคำสั่งแสดงผล value ของหัวแถว ถ้าหากในแถวไม่มีคนจะแสดงคำว่า Empty '''

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

inp = input("Enter Input : ").split(",")

qES = Queue()
qEN = Queue()

for i in inp:
    temp = i.split(" ")
    if temp[0] == "ES":
        qES.enQueue(temp[1])

    elif temp[0] == "EN":
        qEN.enQueue(temp[1])

    elif temp[0] == "D":
        if qEN.isEmpty() and qES.isEmpty():
            print("Empty")
        elif qES.size() != 0:
            print(qES.deQueue())
        else:
            print(qEN.deQueue())
