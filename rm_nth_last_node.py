"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        i=0
        
        while temp is not None:
            i+=1
            temp = temp.next
            
        
        prev = curr = head
        j=0
        
        while j+n != i:
            j+=1
            prev = curr
            curr = curr.next
        
        if prev.next == curr.next and curr.next is None:
            return None
        elif curr.next is not None and i==n:
            head = curr.next
        else:
            prev.next = curr.next
        
        #prev.next = curr.next
        
        return head
        
