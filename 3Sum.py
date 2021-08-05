"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        n = len(nums)
        
        if n<=2:
            return []
        #nums = sorted(nums)
        res=[]
        for i in range(0,n-2):
            for j in range(i+1,n-1):
                """
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k]==0 and sorted([nums[i],nums[j],nums[k]]) not in res:
                        
                        res.append(sorted([nums[i],nums[j],nums[k]]))
                """
                cumsum = nums[i]+nums[j]
                opp = -cumsum
                
                if opp not in nums:
                    break
                else:
                    threeSum = sorted([nums[i],nums[j],opp])
                    if threeSum not in res:
                        res.append(threeSum)
                        break
        
        return res
                    
