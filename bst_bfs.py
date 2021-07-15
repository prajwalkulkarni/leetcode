class Node:
    
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = None
        self.right = None
    

def createNode(data):
    
    node = Node(data)
    
    return node
    

def insert(root,data):
    if root is None:
        return createNode(data)
    
    if root.data == data:
        #root = createNode(data,root.left,root.right)
        return root
    
    elif root.data > data:
        root.left = insert(root.left,data)
    else:
        root.right = insert(root.right,data)
    
    return root


def height(root):
    i=0
    j=0
    temp =root
    rtemp = root
    if root is None:
        return 0
    while temp is not None:
        i+=1
        temp = temp.left
    while rtemp is not None:
        j+=1
        rtemp = rtemp.right
    
    if i>j:
        return i
    else:
        return j
    
def inOrder(root):
    
    if root is not None:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)


def levelOrder(root):
    h = height(root)
    
    for j in range(h+1):
        printCurrentLevel(root,j)

def printCurrentLevel(root,h):
    if root is None:
        return
    if h ==1:
        print(root.data)
    if h>1:
        printCurrentLevel(root.left,h-1)
        printCurrentLevel(root.right,h-1)
n = input("Enter elements")

i=0
r= None
head = None
while i<int(n):
    data = input("Enter data")
    head = insert(head,int(data))
        
    i+=1


levelOrder(head)
#inOrder(head)
