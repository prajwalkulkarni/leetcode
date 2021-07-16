"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = list(s)
        highest=['']
        substr=[]
        forward=[]
        backward=[]
        
        if s[::] == s[::-1]:
            return s
        for i in range(0,len(s)):
            k=0
            
            for j in range(i,len(s)):
                
                forward = str(s[i:len(s)-k])
                backward = forward[::-1]
                #backward+=s[k]
                k+=1
                
                if forward == backward:
                    
                    highest.append(str(forward))
        
        return max(highest,key=len)
                

