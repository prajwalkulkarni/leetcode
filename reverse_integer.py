"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        self.x = x
        y = list(str(x))
        
        if x < 0:
            y=y[1:]
            y=y[::-1]
            ele = ''
            for c in y:
                ele+=c
            f = int(ele)
            print(f)
            if -f < math.pow(-2,31):
                return 0
            return -f
        else:
            y=y[::-1]
            ele = ''
            for c in y:
                ele+=c
            f = int(ele)
            if f >(math.pow(2,31)-1):
                return 0
            return f
            
            
        
