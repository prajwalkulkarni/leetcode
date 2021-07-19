"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        flag=0
        
        if target in nums:
            return nums.index(target)
        else:
            
            for index,i in enumerate(nums):
                if i>target:
                    flag=1
                    return index
            
            if flag==0:
                return len(nums)
        
