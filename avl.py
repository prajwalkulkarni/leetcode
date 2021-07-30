class Node:
    
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
    

def createNode(key):
    
    node = Node(key)
    
    return node


def insert(root,data):
    
    if root is None:
        return createNode(data)
    
    
    elif data < root.val:
        root.left = insert(root.left,data)
        
    else:
        root.right = insert(root.right,data)
    
    root.height = 1 + max(getHeight(root.left),getHeight(root.right))
    
    balance = getBalance(root)
    
    #ll
    if balance<-1 and data<root.left.val:
        return rotateRight(root)
    
    #rr
    elif balance>1 and data>root.right.val:
        return rotateLeft(root)
    
    #lr
    elif balance<-1 and data>root.left.val:
        root.left = rotateLeft(root.left)
        return rotateRight(root)
    
    #rl
    elif balance>1 and data<root.right.val:
        root.right = rotateRight(root.right)
        return rotateLeft(root)
    
    
    
    
    
    return root

def rotateRight(z):
    
    y = z.left
    t2 = y.right
    
    y.right = z
    z.left=t2
    
    z.height = 1+max(getHeight(z.left),getHeight(z.right))
    y.height = 1+max(getHeight(y.left),getHeight(y.right))
    
    
    return y

def rotateLeft(z):
    
    y = z.right
    t2=y.left
    
    y.left = z
    z.right = t2
    
    z=1+max(getHeight(z.left),getHeight(z.right))
    y=1+max(getHeight(y.left),getHeight(y.right))
    
    
    return y
def getHeight(root):
    
    if not root:
        return 0
    
    return root.height

def getBalance(root):
    
    if not root:
        return 0
    
    return getHeight(root.right)-getHeight(root.left)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
def levelOrder(root):
    h = getHeight(root)
    
    for j in range(1,h+1):
        printCurrentLevelOrder(root,j)

def printCurrentLevelOrder(root,level):
    if root is None:
        return None
    
    if level ==1:
        print(root.val)
    if level>1:
        printCurrentLevelOrder(root.left,level-1)
        printCurrentLevelOrder(root.right,level-1)

root = None

root = insert(root,10)
root = insert(root,20)
root = insert(root,30)
root = insert(root,40)
root = insert(root,50)
root = insert(root,25)

#levelOrder(root)
inorder(root)
