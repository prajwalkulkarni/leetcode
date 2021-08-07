class Node:
    
    depth=0
    loT=[]      #If breadth first search needs to be grouped as subarray level wise
    tracker=[]
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
        if self.depth not in self.tracker:           #Check if current level of present node not already there(another node with same level)->new level
            self.loT.append([root.data])             #create a new subarray and add to it
            self.tracker.append(self.depth)          #add current level
        else:
            self.loT[self.depth].append(root.data)   #If a node of same level already there, add current node to already present level
            
    if h>1:
        self.depth+=1                   #Identify level of current node
        printCurrentLevel(root.left,h-1)
        printCurrentLevel(root.right,h-1)
        self.depth-=1                   #identify level of current node
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

























class Node:
    
    def __init__(self,left,right,val):
        self.left = left
        self.right = right
        self.val=val
    

def createNode(val):
    
    node = Node(None,None,val)
    
    return node 



def insert(root,key):
    
    if root is None:
        return createNode(key)
    
    elif key>root.val:
        root.right = insert(root.right,key)
    else:
        root.left = insert(root.left,key)
    
    return root

def getHeight(root):
    temp = root
    rtemp = root
    i=0
    j=0
    
    while temp is not None:
        i+=1
        temp=temp.left
    
    while rtemp is not None:
        j+=1
        rtemp = rtemp.right
    
    if i>j:
        return i
    elif j>i:
        return j
    else:
        return i


def currentOrder(root):
    h = getHeight(root)
    #print(h)
    
    for j in range(1,h+1):
        printCurrentLevelOrder(root,j)

def printCurrentLevelOrder(root,level):
    
    if root is None:
        return None
    if level==1:
        print(root.val)
    if level>1:
        printCurrentLevelOrder(root.left,level-1)
        printCurrentLevelOrder(root.right,level-1)


def inorderSuccessor(root):
    
    current = root
    while current.left is not None:
        current = current.left
    
    return current
    
def deleteNode(root,key):
    
    if root is None:
        return root
    
    if key>root.val:
        root.right = deleteNode(root.right,key)
    elif key<root.val:
        root.left = deleteNode(root.left,key)
    
    else:
        
        if root.left is None:
            temp = root.right
            root = None
            return temp
        
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        #two children
        
        temp = inorderSuccessor(root.right)
        print(temp,temp.val)
        root.val = temp.val
        
        root.right = deleteNode(root.right,temp.val)
    return root
    
n = input("How many elements")

i=0
root = None
while i<int(n):
    
    data = input("Enter number")
    root = insert(root,int(data))
    i+=1

currentOrder(root)   


rm = input("Enter node to be deleted")

deleteNode(root,int(rm))

currentOrder(root)
        
