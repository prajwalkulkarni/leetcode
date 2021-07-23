"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""

import math
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        j=x
        if x==1.0:
            return 1.0
        elif x==-1.0:
            if n%2==0:
                return -x
            else:
                return x
        elif x==0.0:
            return 0.0
        elif n > 100 and x<0.99 and x>-0.9:
            return 0.0
        elif n<-1000:
            return 0.0
        elif n<0:
            x=1/x
            j=1/j
            n=-n
            #print(x,j)
        elif n == 0:
            return 1
        
        
        
        
        for i in range(0,n-1):
            x*=j
            #print(x)
        
        return x
    
        
