''' ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ '''

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
         
    def printTree(self, node, level = 0): #inOrder
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
