"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def createNode(val,nextVal):
    node = ListNode(val,nextVal)
    return node
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = 0
        flag = 0
        ans=[]
        
        while l1 is not None or l2 is not None:
            a = 0 if l1 == None else l1.val
            b = 0 if l2 == None else l2.val
            
            if a+b<10:
                
                if flag == 1:
                    res=a+b+flag
                    flag=0
                    if res>=10:
                        res = res%10
                        flag=1
                    
                else:
                    res=a+b
                    
                    
                    
                    
                ans.append(res)
                res=0
                
            
                
            elif a+b>=10:
                
                if flag == 1:
                    res= ((a+b)%10)+flag
                else:
                    res= ((a+b)%10)
                    
                
                flag=1
                ans.append(res)
                res=0
            elif a is 0 or b is 0 and flag is not 0:

                    res= a+b+flag
                    if res>=10:
                        res = res%10
                        ans.append(res)
                        res = 0
                        flag = 1
                    else:
                        ans.append(res)
                        res=0
                        #flag = 0
                    
                
            
            
            if l1 is not None:
                l1 = l1.next
            
            if l2 is not None:
                l2 = l2.next
            
        
        
        if flag ==1:
            ans.append(1)
        head = None
        ans = [str(i) for i in ans]
        ans.reverse()
        ans = [int(i) for i in ans]
        
        #fans = ans.reverse()
        #print(type(fans))
        #ans = 
        for i in ans:
            
            head = createNode(i,head)
        
        
            
        return head
            
            
