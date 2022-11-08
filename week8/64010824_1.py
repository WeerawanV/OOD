''' กฤษฎาได้ค้นพบเม็ดถั่ววิเศษที่เมื่อโยนลงดินแล้วถั่วจะสามารถเติบโตขึ้นและกลายเป็น Binary Search Tree (BST) ได้ โดยงานของนักศึกษาก็คือนักศึกษาจะต้องสร้าง BST ตามลำดับของข้อมูลนำเข้าซึ่งเป็น
ตัวเลขจำนวนเต็มที่ไม่ซ้ำกันเลย โดยในการใส่ค่าในแต่ละครั้งจะกลับมาที่ Root of BST เสมอ  แล้วท่องต้นไม้ไปทางซ้ายด้วยคำสั่ง "L" หรือท่องต้นไม้ไปทางขวาด้วยคำสั่ง "R" จนกว่าจะถึงตำแหน่งที่เหมาะสมที่
จะใส่ข้อมูลแล้วจึงพิมพ์ "*" เพื่อใส่ข้อมูลลงไปในต้นไม้  จงเขียนโปรแกรมเพื่อแสดงคำสั่งการท่องต้นไม้ในการใส่ข้อมูลทีละค่าตามลำดับของข้อมูลนำเข้า '''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root == None:
            print("*")
            self.root = Node(data)
        else :
            root = self.root
            while True:
                if data < root.data:
                    if root.left == None:
                        root.left = Node(data)
                        print("L*")
                        break
                    else:
                        print("L" ,end="")
                        root = root.left
                else:
                    if root.right == None:
                        root.right = Node(data)
                        print("R*")
                        break
                    else:
                        print("R" ,end="")
                        root = root.right
        return self.root

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(0, len(inp)):
    root = T.insert(inp[i])
