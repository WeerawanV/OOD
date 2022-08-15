class Calculator :

    def __init__(self,val):
        self.val = val

    def __add__(self,other):
        ans = self.val + other.val
        return ans

    def __sub__(self,other):
        ans = self.val - other.val
        return ans

    def __mul__(self,other):
        ans = self.val * other.val
        return ans

    def __truediv__(self,other):
        ans = self.val / other.val 
        return ans

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")