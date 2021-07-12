"""
Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq=[]
        longest=[]
        length = 0
        
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if s[j] not in freq:
                    length+=1
                    freq.append(s[j])
                else:
                    longest.append(length)
                    substr=''
                    freq=[]
                    length=0
                    break
                    
        longest.append(length)
        
        return max(longest)
                
            
        
