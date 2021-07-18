"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        self.numRows = numRows
        self.s = s
        
        if numRows == 1 or numRows>=len(s):
            return s
        
        s = list(s)
        concat = [[]for i in xrange(numRows)]
        
        row=0
        direction = 0
        for i in range(0,len(s)):
            concat[row].append(str(s[i]))
            
            if row%(numRows-1)==0:
                if direction==0:
                    direction = 1
                else:
                    direction = 0
                
            if direction==1:
                row+=1
            else:
                row-=1
            
        
        
        for i in xrange(len(concat)):
            concat[i] = ''.join(concat[i])
            
        return ''.join(concat)
            
            
