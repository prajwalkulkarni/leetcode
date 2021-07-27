"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

Input: n = 16
Output: true
"""

import math
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n==0:
            return False
        elif n==1 or n==4:
            return True
        
        elif n<0:
            return False
        else:
            y=4
            x= 4
            flag=False
            
            while x<=n:
                if x>n:
                    break
                elif x==n:
                    flag=True
                    break
                x *= 4
                
            return flag
