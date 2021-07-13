"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    inorder=[]
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        Solution.inorder=[]
        
        #inorder=[]
        self.recursive(root)
        
        return Solution.inorder
        
        
    def recursive(self,root):
        
        if root is not None:
            
            self.recursive(root.left)
        
            Solution.inorder.append(root.val)
        
            self.recursive(root.right)
        
"""
Pre-oder traversal
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        Solution.inorder=[]
        
        #inorder=[]
        self.recursive(root)
        
        return Solution.inorder
    
    def recursive(self,root):
        
        if root is not None:
            
            
            Solution.inorder.append(root.val)
            self.recursive(root.left)
        
            
        
            self.recursive(root.right)
        
        
        
    
