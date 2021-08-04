"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        row = len(grid)
        col= len(grid[0])
        total=0
        
        for i in range(0,row):
            for j in range(0,col):
                
                if grid[i][j] == 1:
                    total+=4
                    if grid[i][j]==1 and j>=1 and grid[i][j-1]==1:
                        #print("left")
                        total-=2
                        #total-=2
                
                    if grid[i][j]==1 and i>=1 and grid[i-1][j]==1:
                        #print("up")
                        total-=2
                        #total-=2
                #print(total)
        
        return total
        
