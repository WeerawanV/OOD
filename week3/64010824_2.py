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
    