"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        di = len(nums) - 1
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>=di-i:
                di = i
                
        
        return di==0
    """
    def jumpGame(self,nums,pos,visited):
        
        #toPos = skip
        if pos==len(nums)-1:
            return True
        
        if nums[pos]==0:
            return False
        
        if pos>len(nums)-1:
            return False
        
        if pos in visited:
            return False
        length = nums[pos]
        
        for i in range(1,length+1):
            if self.jumpGame(nums,pos+i,visited):
                return True
            
             
        
        visited.append(pos)
        return False
        #return self.jumpGame(nums,pos+1)
        #return False
    """
        
