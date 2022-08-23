'''ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ STACK ในการแก้ปัญหา

A  <value>  ให้นำ value ไปใส่ใน STACK และทำการแสดงผล Size ปัจจุบันของ STACK

P                 ให้ทำการแสดงผลของvalueที่อยู่ท้ายสุดและindexของvalueนั้นจากนั้นทำการ Pop_Stack ถ้าหากไม่มี value อยู่ใน Stack ให้แสดงผลเป็น  -1

*** ในตอนสุดท้ยถ้าหากใน Stack ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty '''

class Stack :
    
    def __init__ (self,list = None):
        if list == None :
            self.items = []
        else :
            self.items = list
        self.size = len(self.items)
    
    def push(self, n):
        self.items.append(n)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.items.pop() 

    def size(self):
        return len(self.items)

num = input("Enter Input : ").split(",")
s = Stack()

for i in num:
    if i[0] == "A" :
        int,temp = i.split(" ")
        s.push(temp)
        print("Add =" , temp , "and Size =" , s.size)
    elif i == "P" :
        if s.size == 0 :
            print("-1")
        else :
            print("Pop =", s.pop(), "and Index =" , s.size)

if s.size == 0 :
    print("Value in Stack = Empty")
else :
    print("Value in Stack =" , *s.items)
