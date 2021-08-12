"""
Traverse boundary nodes of a bst.
"""


def traverseLeaves(root):
  
  if root:
    traverseLeaves(root.left)
    
    if root.left is None and root.right is None:
      print(root.data)
    traverseLeaves(root.right)

    
def boundaryLeft(root):
  if root:
    
    if root.left:
      print(root.data)
      boundaryLeft(root.left)
    
    elif root.right:
      print(root.data)
      boundaryLeft(root.right)

def boundaryRight(root):
  if root:
    
    if root.right:
      print(root.data)
      boundaryRight(root.right)
     
    elif root.left:
      print(root.data)
      boundaryRight(root.left)

def boundaryTraversal(root):
  
  if root:
    print(root.data)
    boundaryLeft(root)
    
    traverseLeaves(root)
    
    boundaryRight(root)
 
