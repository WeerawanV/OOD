''' หาว่าค่าแรกที่ใส่เข้าไปอยู่ที่ตำแหน่งใดใน BST '''

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
    
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return self.root
        root = self.root
        while True:
            if data < root.data:
                if root.left == None:
                    root.left = Node(data)
                    return self.root
                root = root.left
            else:
                if root.right == None:
                    root.right = Node(data)
                    return self.root
                root = root.right
         
    def printTree(self, node, level = 0): 
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkpos(self,data):
        if self.root.data == data:
            print("Root")
            return

        cur = self.root 
        while cur != None:
            if cur.data < data:
                cur = cur.right
            elif cur.data > data:
                cur = cur.left
            elif cur.data == data:
                if (cur.left == None) and (cur.right == None):
                    print("Leaf")
                    return
                else:
                    print("Inner") 
                    return

        print("Not exist")
        return

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0])
