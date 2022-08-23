class Stack :

    def __init__(self,list = None) :
        if list == None :
            self.items = []
        else :
            self.items = list

    def isEmpty(self) :
        return self.items == []

    def push(self,data) :
        self.items.append(data)
    
    def pop(self) :
        return self.items.pop()
 
    def size(self) :
        return len(self.items)

    def peek(self) :
        return self.items[-1]

def infix2postfix(exp) :

    S = Stack()
    output = ""
    Operators = set(['+', '-', '*','(', ')', '/', '^']) 
    Priority = {'+':1, '-':1, '*':2, '/':2, '^':3}

    for i in exp :
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
    
    return output

print(" ***Infix to Postfix***")
token = input("Enter Infix expression : ")
print("PostFix : ")
print(infix2postfix(token))