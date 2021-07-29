"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
"""


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
       
    
        if len(ratings) == 0:
            return 0
        elif list(set(ratings))==1:
            return len(ratings)
        
        
        maximum = max(ratings)
        maxNo = len(ratings)
        minimum = [1 for i in range(len(ratings))]
        
        
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                minimum[i]+=minimum[i-1]
            elif ratings[i-1]>ratings[i]:
                j=i-1
                k=0
                
                while j+1<=len(ratings)-1 and ratings[j]>ratings[j+1] :
                    #print("one")
                    k+=1
                    j+=1
                
                
                    
                if not minimum[i-1]>k:
                    minimum[i-1]=k+1
            
        
        return sum(minimum)
