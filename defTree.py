class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

def insert(self,data):
  if self.root == None:
    self.root = Node(data)
  else:
    root = self.root
    while True:
      if data < root.data:
        if root.lefr == None:
          root.left = Node(data)
          break
        else:
          root = root.left
      else:
        if root.right == None:
          root.right = Node(data)
          break
        else:
          root = root.right
  return self.root

def delete(self,node,data):
  if self.root == None:
    return
  
  elif self.root.data == data:
    if self.root.left == None and self.root.roght == None:
      self.root = None
    elif self.root.left == None:
      self.root = self.root.right
    elif self.root.right == None:
      self.root = self.root.left

  if node.data != data:
    if data < node.data:
      node.left = self.delete(node.left,data)
    else: 
      node.right = self.delete(node.right,data)
  else:
    if node.left == None:
      node = node.right
      return node
    elif node.right == None:
      node = node.left
      return node
    else:
      now = node.right
      while node.left != None:
        now = now.left
      node.data = now.data
      node.right = self.delete(node.right,data)
  return node

def check(root):
  def isBST(node,min = -1 ,max = 101):
    if node.data <= min or node.data >= max:
      return False

    left = True
    right = True

    if node.left != None:
      left = isBST(node.left,min,node.data)

    if node.right != None:
      right = isBST(node.right,node.data,max)

    return left and right

  if root == None:
    return True

  return isBST(root)

def getMin(self):
  now = self.root
  while now.left != None:
    now = now.left
  return now.data

def getMax(self):
  now = self.root
  while now.right != None:
    now = now.right
  return now.data

def father(r,data):
  prev = None
  if r == None:
    return "Not Found Data"
  else: 
    if r.data == data:
      return "None Because " + str(data) + " is Root"

  #case find
  cur = r
  while cur != None:
    if cur.data < data:
        prev = cur
        cur = cur.right
    elif cur.data > data:
        prev = cur
        cur = cur.left
    elif cur.data == data:
        return prev.data

  return "Not Found Data"
  
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
