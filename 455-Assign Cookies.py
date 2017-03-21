'''
 Assume you are an awesome parent and want to give your children some cookies. 
 But, you should give each child at most one cookie. 
 Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; 
 and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. 
 Your goal is to maximize the number of your content children and output the maximum number.

Note:
You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.

Example 1:

Input: [1,2,3], [1,1]

Output: 1

Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

Example 2:

Input: [1,2], [1,2,3]

Output: 2

Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
'''

# ---------------------------------------------------------------------------------------------------
# 需要进一步优化，循环嵌套循环效率太低，这样写Runtime: 759 ms
#
# ---------------------------------------------------------------------------------------------------

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count = 0
        g.sort()
        s.sort()
        for i in g:
            for j in s:
                if i <= j:
                    s.remove(j)
                    count += 1
                    break
        return count


S = Solution()
print(S.findContentChildren([1,2], [1,2,3]))
print(S.findContentChildren([1,2,3], [1,1]))
print(S.findContentChildren([2,3,5], [1,2,3,4]))

# ---------------------------------------------------------------------------------------------------

# --------------------------------------Best Result 1------------------------------------------------
# # 时间复杂度：O(nlogn)
# class Solution(object):
#     def findContentChildren(self, g, s):
#         """
#         :type g: List[int]
#         :type s: List[int]
#         :rtype: int
#         """
#         g.sort()
#         s.sort()
        
#         childi = 0
#         cookiei = 0
        
#         while cookiei < len(s) and childi < len(g):
#             if s[cookiei] >= g[childi]:
#                 childi += 1
#             cookiei += 1
        
#         return childi
# ---------------------------------------------------------------------------------------------------

# --------------------------------------Best Result 2------------------------------------------------
# # 时间复杂度：O(nlogn)
# # 空间复杂度：O(1)
# class Solution(object):
#     def findContentChildren(self, g, s):
#         g.sort()
#         s.sort()
#         res = 0
#         i = 0
#         for e in s:
#             if i == len(g):
#                 break
#             if e >= g[i]:
#                 res += 1
#                 i += 1
#         return res
# ---------------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------------
# class Solution(object):
#     def findContentChildren(self, g, s):
#         """
#         :type g: List[int]
#         :type s: List[int]
#         :rtype: int
#         """
        


# S = Solution()
# print(S.findContentChildren([1,2], [1,2,3]))
# print(S.findContentChildren([1,2,3], [1,1]))
# print(S.findContentChildren([2,3,5], [1,2,3,4]))

# ls = [1,3,5,4,2]
# ls.sort()
# del ls[0]
# print(ls)

# ---------------------------------------------------------------------------------------------------