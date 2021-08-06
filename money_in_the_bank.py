"""
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

 

Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
Example 2:

Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
Example 3:

Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
"""
class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n<=7:
            return (n*(n+1))/2
        
        sevens = n//7
        
        k=0
        total=0
        while k<sevens:
            #print("x")
            offset = k+7
            
            total+=(offset*(offset+1)/2)
            
            if k>0:
                total-= (k*(k+1)/2)
            #print(total)
            k+=1
        
        remainder = n%7
        
        #actualSum=0
        
        
        for i in range(sevens+1,sevens+remainder+1):
            total+= i
        
        return total
        
