"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3=None
        
        while l1 is not None or l2 is not None:
            
            if l1 is not None and l2 is not None:
                
                if l1.val == l2.val:
                    l3 = ListNode(l2.val,l3)
                    l3 = ListNode(l1.val,l3)
                    l1 = l1.next
                    l2 = l2.next
                elif l1.val > l2.val:
                    l3 = ListNode(l2.val,l3)
                    l2 = l2.next
                else:
                    l3 = ListNode(l1.val,l3)
                    l1 = l1.next
            elif l1 is None and l2 is not None:
                l3 = ListNode(l2.val,l3)
                l2 = l2.next
            elif l1 is not None and l2 is None:
                l3 = ListNode(l1.val,l3)
                l1 = l1.next
            
        
        
            
        curr = l3
        prev = None
       
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        curr = prev
        return curr
            
            
