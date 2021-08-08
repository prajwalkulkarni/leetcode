"""
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    #sortedList=[]
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i=0
        temp = head
        while temp is not None:
            i+=1
            temp=temp.next
        
        sortedList = [0 for j in range(i)]
        
        temp = head
        i=0
        while temp is not None:
            sortedList[i] = temp.val
            temp = temp.next
            i+=1
        
        #print(sortedList)
        
        sortedList = self.mergeSort(sortedList)
        
        i=0
        temp = head
        while temp is not None:
            temp.val = sortedList[i]
            temp = temp.next
            i+=1
        
        return head
    
    def mergeSort(self,nums):
        
        l = 0
        r = len(nums)
        if len(nums)>1:
            
            
            
            mid = (l+r)//2
            
            leftArr = nums[:mid]
            rightArr = nums[mid:]
            
            self.mergeSort(leftArr)
            self.mergeSort(rightArr)
            
            i=j=k=0
            
            while i<len(leftArr) and j<len(rightArr):
                if leftArr[i]<rightArr[j]:
                    nums[k] = leftArr[i]
                    i+=1
                    k+=1
                else:
                    nums[k] = rightArr[j]
                    j+=1
                    k+=1
            
            while i<len(leftArr):
                nums[k]=leftArr[i]
                i+=1
                k+=1
            
            while j<len(rightArr):
                nums[k] = rightArr[j]
                j+=1
                k+=1
        return nums
        
        
