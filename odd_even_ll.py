"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        
        n=0
        temp = head
        
        while temp is not None:
            n+=1
            temp = temp.next
        
        if n ==1 :
            return head
        arr = [-69 for i in range(n)]
        
        even,odd,traverse = head,head.next,head
        i=0
        
        while even is not None:
            arr[i] = even.val
            if even.next is None:
                break
            even = even.next.next
            i+=1
        if n%2==0:
            j=i
        else:
            j=i+1
        while odd is not None:
            arr[j] = odd.val
            #print(j)
            if odd.next is None:
                break
            odd = odd.next.next
            j+=1
        
        k=0
        while traverse is not None:
            traverse.val = arr[k]
            k+=1
            traverse=traverse.next
        
        return head
        
