'''ให้รับ Input เป็น  Infix  และแสดงผลลัพธ์ออกมาเป็น  Postfix   โดยจะมี Operator  5  แบบ  ได้แก่  +   -   *   /   ^

class Stack:

    def __init__(self):

    def push(self, value):

    def pop(self):

    def size(self):

    def isEmpty(self):

inp = input('Enter Infix : ')

S = Stack()

print('Postfix : ', end='')

### Enter Your Code Here ###

while not S.isEmpty():

    print(S.pop(), end='')

print()
'''

class Stack:
    
    items = []
    
    def __init__(self , list = None):
        if list == None :
            self.items = []
        else :
            self.items = list

    def push(self, n):
        self.items.append(n)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

inp = input('Enter Infix : ')
S = Stack()

output = " "
print('Postfix :', end='')

Operators = set(['+', '-', '*','(', ')', '/', '^']) 
Priority = {'+':1, '-':1, '*':2, '/':2, '^':3}

for i in inp :
    if i not in Operators :
        output += i
    elif i == "(" :
        S.push("(")
    elif i == ")" :
        while (not S.isEmpty()) and S.peek() != "(" :
            output += S.pop()
        S.pop()
    else :
        while (not S.isEmpty()) and S.peek() != "(" and Priority[i] <= Priority[S.peek()] :
            output += S.pop()
        S.push(i)
        
while not S.isEmpty():

    output += S.pop()

print(output)
