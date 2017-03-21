'''
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

给定在平面中的所有成对不同的n个点，“飞旋镖”是点（i，j，k）的元组，使得i和j之间的距离等于i和k之间的距离（元组的顺序 ）。

查找飞旋镖的数量。 您可以假设n最多为500，点的坐标都在[-10000，10000]（含）范围内。
'''

# -------------------------------------------------------------------------------------------------
# 很好的题目，看了结果还好久才明白，而且题意开始也没有理解清楚
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        #循环两次，也就是要对比每对数与其他数之间的距离
        for i in range(len(points)):
        	#创建字典是为了记录同样的距离数出现了几次，key是距离的绝对值，value是出现的次数
            ans = {}
            for j in range(len(points)):
            	#dis_x与dis_y代表两点间距离的平方数
                dis_x = ((points[i][0] - points[j][0])**2)
                dis_y = ((points[i][1] - points[j][1])**2)
                #记录距离数出现的次数
                ans[abs(dis_x + dis_y)] = 1 + ans.get(abs(dis_x + dis_y),0)
            #统计出现次数的和，这个只能在内循环中统计，如果放到外面值会大于真实值
            for n in ans:
#                res += (ans[n]-1)*2    这样写是不对的
                res += ans[n] * (ans[n]-1) #这句话代表每次的结果都可以将两个数调换位置，所以求和要求双倍的，也就是求和公式2S = n*(n-1), (n-1)次n相加
        return res

S = Solution()
print(S.numberOfBoomerangs([[0,0],[1,0],[2,0]]))

      
# -------------------------------------------------------------------------------------------------



# ------------------------------------------草稿---------------------------------------------------
# def numberOfBoomerangs():
#     """
#     :type points: List[List[int]]
#     :rtype: int
#     """
#     # points = [[0,0],[1,0],[2,0]]
#     # points = [[1,0],[3,0],[5,0],[7,0],[9,0]]
#     points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
#     res = 0
#     for i in range(len(points)):
#         ans = {}
#         for j in range(len(points)):
#             dis_x = ((points[i][0] - points[j][0])**2)
#             dis_y = ((points[i][1] - points[j][1])**2)
#             ans[abs(dis_x + dis_y)] = 1 + ans.get(abs(dis_x + dis_y),0)
#         #     print('第%s次中的第%s内循环ans的值=%s'%(i,j,ans))
#         # print('----'*10)
#         for n in ans:
#             # res += (ans[n]-1)*2
#             res += ans[n] * (ans[n]-1)
#     return res     

# print(numberOfBoomerangs())
# # numberOfBoomerangs()
# -------------------------------------------------------------------------------------------------




# --------------------------------------Best Result------------------------------------------------
# def numberOfBoomerangs(self, points):    
#     res = 0
#     for p in points:
#         cmap = {}
#         for q in points:
#             f = p[0]-q[0]
#             s = p[1]-q[1]
#             cmap[f*f + s*s] = 1 + cmap.get(f*f + s*s, 0)
#         for k in cmap:
#             res += cmap[k] * (cmap[k] -1)
#     return res

# print(numberOfBoomerangs([[0,0],[1,0],[2,0]]))
# -------------------------------------------------------------------------------------------------

