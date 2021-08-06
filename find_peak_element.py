"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""


#Can use binary search or regular for loop to find peak element in an unsorted array

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        j=0
        for i in range(1,len(nums)-1):
            #print(i)
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                j=i
                break
        
        #return j
        if j==0:
            return nums.index(max(nums))
        else:
            return j
        """
        ans=-1
        low = 0
        high = len(nums)
        
        while low<=high:
            m = (low+high)//2
            
            if nums[m]>nums[m-1] and nums[m] >nums[m+1]:
                ans=m
                break
            elif nums[m]>nums[m-1] and nums[m]<nums[m+1]:
                high = m-1
            elif nums[m]>nums[m+1] and nums[m]<nums[m-1]:
                low = m+1
        return ans
