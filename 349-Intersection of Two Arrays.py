'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:

    Each element in the result must be unique.
    The result can be in any order.

给定两个数组，写一个函数来计算它们的交集。

例：
给定nums1 = [1,2,2,1]，nums2 = [2,2]，return [2]。

注意：

     结果中的每个元素必须是唯一的。
     结果可以是任何顺序。
'''

# -------------------------------------------------------------------------------------------------
# 
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1=set(nums1)
        nums2=set(nums2)
        return list(nums1&nums2)

S = Solution()
print(S.intersection([1, 2, 2, 1],[2, 2]))
print(S.intersection([1, 2, 3, 4],[3, 4]))
print(S.intersection([1, 1, 1, 1],[1, 1, 1]))        
# -------------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------------
#有错误
# class Solution(object):
#     def intersection(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         i = 0
#         j = 0
#         res = []
#         while (i < len(nums1)) and (j < len(nums2)):
#             if nums1[i] == nums2[j]:
#                 print('i = %s ; j = %s'% (i,j))
#                 i += 1
#                 j += 1
#                 res.append(nums2[j])   
#             else:
#                 j += 1
#         return res             

# S = Solution()
# print(S.intersection([1, 2, 2, 1],[2, 2]))
# print(S.intersection([1, 2, 3, 4],[3, 4]))
# print(S.intersection([1, 1, 1, 1],[1, 1, 1]))  
# -------------------------------------------------------------------------------------------------