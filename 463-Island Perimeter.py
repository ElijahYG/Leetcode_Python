'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. 
Grid cells are connected horizontally/vertically (not diagonally). 
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). 
The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
'''

# ---------------------------------------------------------------------
'''
步骤：
	1、先找出所有的1，先都乘4
	2、找所有相邻的1，包括上下左右，每遇到一个相邻就减2
'''
# ---------------------------------------------------------------------
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #计算所有的1，乘以4也就是正方形的四个边
        num_for_1 = 0
        res = 0
        for x in grid:
            for y in x:
                if y == 1:
                    num_for_1 += 1
        res = num_for_1 * 4

        #先找所有的内层列表中左右相邻的1，每次遇到相邻的就减去2
        for x in range(len(grid)):
            for y in range(len(grid[x])-1):
                if (grid[x][y] == 1) and (grid[x][y+1] == 1):
                    res -= 2
        
        #再找所有的外层列表中上下相邻的1，每次遇到相邻的就减去2
        for x in range(len(grid)-1):
            for y in range(len(grid[x])):
                if (grid[x][y]) == 1 and (grid[x+1][y] == 1):
                    res -= 2
        return res

S = Solution()
# print(S.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]] ))
print(S.islandPerimeter([[0,1]]))



# ---------------------------------Method 2---------------------------------------
# class Solution(object):  
#     def islandPerimeter(self, grid):  
          
#         res = 0  
          
#         for i in grid:  
#             res += sum(i)  
#         g= grid  
#         res *= 4  
          
#         i,j = 0,0  
          
#         while i < len(g):  
#             j = 0  
#             while j < len(g[0]):  
#                 if j + 1< len(g[0]) and g[i][j] == 1 and g[i][j+1] == 1:  
#                     res -= 2  
#                 j += 1  
#             i += 1  
              
#         i,j = 0,0  
#         while i < len(g[0]):  
#             j = 0  
#             while j < len(g):  
#                 if j + 1 < len(g) and g[j][i] == 1 and g[j+1][i] == 1:  
#                     res -= 2  
#                 j += 1  
#             i += 1  
#         return res 

# S = Solution()
# print(S.islandPerimeter([[1,1,0,0,0],[0,1,0,0,0],[0,1,1,0,0],[0,1,0,0,0,0],[1,1,1,0,0]]))    
# --------------------------------------------------------------------------------


# ------------------------------草稿-------------------------------------
# #测试数据：答案为16
# grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]] 
# #测试数据：答案为20
# #grid = [[1,1,0,0,0],[0,1,0,0,0],[0,1,1,0,0],[0,1,0,0,0,0],[1,1,1,0,0]]


# num_for_1 = 0
# res = 0
# for x in grid:
# 	# print('x.count(1)的个数=%s'%x.count(1))
# 	for y in x:
# 		if y == 1:
# 			num_for_1 += 1
# res = num_for_1 * 4
# # print('res初始值是 %s'%res)

# for x in range(len(grid[0])):
# 	for y in range(len(grid[x])):
# 		if (grid[x][y] == 1) and (grid[x][y+1] == 1):
# 			res -= 2
# 			# print('第一个循环中x值是 %s'%x)
# 			# print('第一个循环中y值是 %s'%y)
# 			# print('第一个循环中的res值是 %s'%res)

# # print('==='* 20)
# for x in range(len(grid)-1):
# 	for y in range(len(grid[x])):
# 		if (grid[x][y]) == 1 and (grid[x+1][y] == 1):
# 			res -= 2		
# 			# print('第一个循环中的grid[x][y]值是 %s,grid[x+1][y]值是 %s'%(grid[x][y],grid[x+1][y]))
# 			# print('---'* 20)	
# 			# print('第二个循环中的res值是 %s'%res)

# print(res)
# -------------------------------------------------------------------

# ------------------------------------------------------------------- 
## 所有边的总数
# def sum(n):
##    a = (4 * n * n ) - 2*(n * (n - 1)) 
#     a = 2 * n * (n + 1)
#     print(a)

# sum(3) 
# -------------------------------------------------------------------  

# grid = [[0,1]]

# print(len(grid)) 
# print(len(grid[0]))

   