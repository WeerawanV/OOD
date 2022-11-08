class TreeNode(object): 
    def __init__(self, data): 
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.data)
  
class AVL_Tree(object): 
    def __init__(self):
        self.root = None

    def insert(self,node,data):
        if node == None:
            return TreeNode(data)
        if data < node.data:
            node.left = self.insert(node.left,data)
        if data >= node.data:
            node.right = self.insert(node.right,data)
        
        balance = self.height(node.left) - self.height(node.right)
        
        if balance > 1 and data < node.left.data: 
            print("Not Balance, Rebalance!")
            return self.rightRotate(node)
        if balance < -1 and data >= node.right.data: 
            print("Not Balance, Rebalance!")
            return self.leftRotate(node)
        if balance > 1 and data >= node.left.data: 
            node.left = self.leftRotate(node.left)
            print("Not Balance, Rebalance!")
            return self.rightRotate(node)
        if balance < -1 and data < node.right.data: 
            node.right = self.rightRotate(node.right)
            print("Not Balance, Rebalance!")
            return self.leftRotate(node)

        return node 

    def height(self,node):
        if node == None:
            return 0
        height_left = self.height(node.left)
        height_right = self.height(node.right)
        if height_left > height_right:
            return height_left + 1
        else:
            return height_right + 1

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        return y
 
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        return y

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.insert(root, int(e))
    printTree90(root)
    print("===============")