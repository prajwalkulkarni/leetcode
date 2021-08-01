"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        """
        j=-1
        
        for i in range(0,n+1):
            
            if i not in nums:
                j=i
                break
        
        return j
        """
        
        actualSum = (n*(n+1))/2
        obtainedSum = sum(nums)
        
        return actualSum-obtainedSum
