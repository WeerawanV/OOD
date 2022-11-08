''' ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

โดยมีการป้อน input ดังนี้

i <int> = insert data

d <int> = delete data

หมายเหตุ การลบนั้นจะใช้หลักการของ Inorder Successor และ จำนวน parameter มีได้มากสุด 3 ตัว '''

class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        if self.root == None:
            self.root = Node(val)
            return self.root
        root = self.root
        while True:
            if val < root.data:
                if root.left == None:
                    root.left = Node(val)
                    return self.root
                root = root.left
            else:
                if root.right == None:
                    root.right = Node(val)
                    return self.root
                root = root.right

    def delete(self,r, data):
        if r is None:
            print("Error! Not Found DATA")     
            return

        elif self.root.data == data:
            if self.root.left == None and self.root.right == None:
                self.root = None
            elif self.root.left == None and self.root.right != None:
                self.root = self.root.right
            elif self.root.right == None and self.root.left != None:
                self.root = self.root.left

        if r.data != data:
            if r.data > data:
                r.left = self.delete(r.left, data)
            else:
                r.right = self.delete(r.right, data)
        else:
            if r.left is None:
                r = r.right
            elif r.right is None:
                r = r.left
            else:
                cur = r.right 
                while cur.left != None: 
                    cur = cur.left 
                r.data = cur.data
                r.right = self.delete(r.right, cur.data) 
        return r

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

tree = BinarySearchTree()
data = input("Enter Input : ").split(",")

for i in data:
    temp = i.split()
    if temp[0] == "i":
        print("insert" , temp[1])
        tree.insert(int(temp[1]))
        printTree90(tree.root)
    elif i[0] == "d":
        print("delete", temp[1])
        tree.delete(tree.root,int(temp[1]))
        printTree90(tree.root)
