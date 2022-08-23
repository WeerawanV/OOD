'''จงสร้างฟังก์ชัน ManageStack() ในการจัดการตัวเลขที่อยู่ใน Stack โดยที่จะมีคำสั่งดังนี้

A (add) : ทำการเพิ่มตัวเลขเข้าไปใน Stack

P (pop) : ทำการนำเลขสุดท้ายใน Stack ออก ( ถ้า Stack ว่างให้แสดงผล -1 )

D (delete) : ทำการลบตัวเลขที่ต้องการใน Stack ( ถ้า Stack ว่างให้แสดงผล -1 )  

LD (lessthan delete) : ทำการลบตัวเลขที่น้อยกว่าตัวเลขที่กำหนดทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

MD (Morethan delete) : ทำการลบตัวเลขที่มากกว่าตัวเลขที่ต้องการทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

การ Delete ทุกแบบ ถ้าหากไม่มีเลขที่ถูกลบเลย ไม่ต้องแสดงผลอะไรและให้ทำการแสดงผลค่าที่อยู่ใน Stack เมื่อจบโปรแกรม

*** Hint ***
ฟังก์ชัน Delete ต่างๆให้สร้าง Stack ขึ้นมาอีก 1 อันเพื่อใช้เป็น Temp ในการเก็บค่าตัวเลขต่างๆ '''

class Stack:
  def __init__ (self,n = None) :
     if n == None :
       self.list = []
     else :
        self.list = n
  
  def push(self,i):
    self.list.append(i)
  
  def pop(self,s = None):
    if s == None :
      return self.list.pop()
    else:
      return self.list.pop(s)
  
  def isEmpty(self):
    return self.list == []
  
  def size(self):
    return len(self.list)

  def __str__(self):
    return str(self.list)

def ManageStack(list = []):
    
    s = Stack()
    
    for i in list :
        
        temp = i.split()
        
        if temp[0] == "P":
            if s.isEmpty():
                print("-1")
            else:
                print("Pop =" , s.pop())
        
        elif temp[0] == "A":
            s.push(int(temp[1]))
            print("Add =" , temp[1])
        
        elif temp[0] == "D":
            if s.isEmpty():
                print("-1")
            else:
                for i in s.list.copy() :
                    if i == int(temp[1]):
                        print("Delete =", s.pop(s.list.index(i)))
        
        elif temp[0] == "MD":
            if s.isEmpty():
                print("-1")
            else:
                for i in reversed(s.list.copy()):
                    if i > int(temp[1]):
                        print("Delete =", s.pop(s.list.index(i)),"Because" , i , "is more than" , temp[1])
        
        elif temp[0] == "LD":
            if s.isEmpty():
                print("-1")
            else:
                for i in reversed(s.list.copy()):
                    if i < int(temp[1]):
                        print("Delete =", s.pop(s.list.index(i)),"Because" , i , "is less than" , temp[1])
      
    return "Value in Stack = " + str(s)
    
inp = input("Enter Input : ").split(",")
print(ManageStack(inp))
    
