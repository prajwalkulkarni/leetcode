"""
An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.

Given an array points where points[i] = [xstart, xend], return the minimum number of arrows that must be shot to burst all balloons.

 

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
"""

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        
        arrows=0
        flag=0
        bf=0
        minimum=0
        n = len(points)
        points.sort(key=lambda x:x[1])
        i=0
        
        """
        while i<n-1:
            j=i+1
            while j<n:
                if points[i][1]>=points[j][0]:
                    bf=0
                    j+=1
                    
                else:
                    arrows+=1
                    i=j
                    bf=1
                    break
            
            if bf:
                i=j
            else:
                i+=1
        """
        i,j = 1,0
        
        while i<n:
            
            if not points[i][0] <= points[j][1]:
                arrows+=1
                j=i
            i+=1
            
                
        return arrows+1
                    
