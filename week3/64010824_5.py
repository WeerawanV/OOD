'''ที่จอดรถของนาย ก เป็นส่วนที่แรเงาสีฟ้า ส่วนสีแดงเป็นที่ของนาย ข ซี่งเป็นญาติกัน ที่จอดรถของนาย ก และ นาย ข แคบมาก จอดรถได้เรียงเดี่ยว นาย ข ไม่ได้ใช้ที่จอดรถ แต่ อนุญาติให้นาย ก ใช้ที่จอดรถของเขาได้โดยไม่จอดรถแช่ไว้ เนื่องจากซอยแคบ ดังนั้นการมาจอด (arrive) และการรับรถ (depart)จะเป็นลักษณะของ stack เงื่อนไขคือ ในการรับรถ x ใดๆอยากให้ลำดับรถเป็นเหมือนเดิม ดังรูป simulate การจอดรถในที่จอดรถของนาย ก โดยใช้ operation ของ stack ข้างล่างเป็นตัวอย่าง output

การรับ input : รับ input 4 ค่าใน 1 บรรทัดโดยให้แยกโดย " " (space bar) โดยตำแหน่งแรกคือ จำนวนสูงสุดที่รถสามารถจอดได้ในซอยของ นาย ก ตำแหน่งที่สองคือ รถที่จอดอยู่ในซอยของ นาย ก ตำแหน่งที่สามคือ การกระทำเช่น ถ้าเป็น arrive จะทำการเพิ่มรถในซอย ส่วน depart จะทำการเอารถออกจากซอย โดยรถที่จะทำการเพิ่มหรือนำออกนั้นจะเป็น เลขในตำแหน่งที่ 4

***หมายเหตุ ถ้าในซอยไม่มีรถอยู่เลยให้ input = 0 ในตำแหน่งที่ 2***

*** สามารถสร้างได้มากกว่า 1 stack ***

class Stack:

print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()

m,n = int(m),int(n)

### Enter Your Code Here ###
'''

class Stack:
  
  def __init__ (self,n = None) :
    if n == None :
      self.items = []
    else :
      self.items = n
  
  def push(self,i):
    self.items.append(i)
  
  def pop(self,s = None):
    if s == None :
      return self.items.pop()
    else:
      return self.items.pop(s)
  
  def isEmpty(self):
    return self.items == []
  
  def size(self):
    return len(self.items)

  def peek(self):
    if (len(self.items) > 0):
      return self.items[-1]

  def __str__(self):
    return str(self.items)

print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()

m,n = int(m),int(n)

p1 = Stack()
p2 = Stack()

temp1 = s.split(",") #car in soi
temp1 = [int(item) for item in temp1]

if s != "0":
    for d in temp1:
        p1.push(d)

if o == "arrive" :
  if p1.size() < m :
    for c in temp1 :
      if n == c:
        print("car", n, "already in soi")
        break
      else :
        p1.push(n)
        print("car" , n, "arrive! : Add Car" ,n)
        break
  elif p1.size() >= m :
    print("car" , n, "cannot arrive : Soi Full")    

elif o == "depart" :
  for c in temp1 :
    if p1.size() == 0 :
        print("car", n, "cannot depart : Soi Empty")
        break
    elif n != c :
        print("car", n, "cannot depart : Dont Have Car",n)
        break    
    else :
        car = p1.size()
        for i in range(car):
          if p1.peek() != n :
            p2.push(p1.peek())
            p1.pop()
          else :
            p1.pop()
            break
        car2 = p2.size() 
        for i in range(car2) :
          p1.push(p2.peek())
          p2.pop()
        print("car", n, "depart ! : Car" , n, "was remove")
        break
        
print(p1)
