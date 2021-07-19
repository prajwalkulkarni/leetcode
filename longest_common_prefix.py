"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


 class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        self.strs = strs
        
        """     
        longest=''
        
        smallest=min(strs,key=len)
        strs.remove(smallest)
        
        fstrs = ''.join(strs)
        
        flag=0
        
        
        treshold = len(smallest)
        j=0
        while j<treshold:
            #print(smallest[j:treshold])
            if fstrs.count(smallest[j:treshold])==len(strs):
                count=0
                for word in strs:
                    if word[0:len(smallest[j:treshold])] == smallest[j:treshold]:
                        count+=1
                if count == len(strs):
                    flag=1
                    longest = smallest[j:treshold]
                    break

            treshold-=1
           
                
            
        
        return longest
        """
        
        word = strs[0]
        
        for i in range(1,len(strs)):
            treshold=len(word)
            while word not in strs[i][0:treshold]:
                treshold-=1
                word = str(word[0:treshold])
                
            
            
            if not str(word)==str(strs[i][0:len(word)]):
                word=""
            
        
        if word=="":
            return ""
        return word
                
                
            
            
        
