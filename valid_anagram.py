"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        self.s = s
        self.t = t
        
        dict1 = {}
        dict2={}
        i=0
        
        for c in s:
            if c in dict1:
                dict1[c] += 1
            else:
                dict1[c] = 1
        
        for c in t:
            if c in dict2:
                dict2[c] += 1
            else:
                dict2[c] = 1
           
                
        if dict1 == dict2:
            return True
        else:
            return False
