"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        self.height = height
        
        high = 0
        area = 0
        k=0
        
        for index,i in enumerate(height):
            for j in range(index+1,len(height)):
                x = i if i<height[j] else height[j]
                
                area = x*(j-index)
                #print(area)
                if area>high:
                    high = area
            
        
        
        
        return high
                
        
        
        
