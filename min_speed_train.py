"""
"""

from math import ceil

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        n = len(dist)
        if hour <= n - 1:
            return -1
    
        if n - 1 < hour < n:
            p = round(hour - (n - 1), 2)
            maxi = max(dist)
            return max(maxi, ceil(dist[n - 1] / p))
        
        low, high = 1, max(dist)
        ans = None
        while low <= high:
            mid = (low + high) // 2
            hr = 0
            for i in range(n):
                p = dist[i] / mid
                hr += p if i == n - 1 else ceil(p)
            if hr <= hour:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
