"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
"""

class Solution:
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        #self.columnTitle = coulmnTitle
        fanswer = 0
        #answer = titleNumber(coulmnTitle)
        listTitle = list(columnTitle)
        iterCount = len(listTitle)
        if iterCount == 1:
            answer=0
        else:
            answer = 1
            
        
        charToVal = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9
                    ,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18
                    ,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
        
        for i in listTitle:
            print(i)
            answer=1
            for j in range(0,iterCount-1):
                
                answer*=26
            iterCount-=1
            answer*=charToVal[i]
            
            fanswer+=answer
        #answer+=answer
        
        print(fanswer)
        
x = Solution()
x.titleToNumber("ZY")
