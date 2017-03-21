'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
给定两个数组，写一个函数来计算它们的交集。

例：
给定nums1 = [1,2,2,1]，nums2 = [2,2]，return [2,2]。

注意：
结果中的每个元素应显示为在两个数组中显示的次数。
结果可以是任何顺序。
跟进：
如果给定的数组已经排序，该怎么办？ 如何优化您的算法？
如果nums1的大小与nums2的大小相比是什么？ 哪种算法更好？
如果nums2的元素存储在磁盘上，并且内存有限，以致于您无法立即将所有元素加载到内存中，该怎么办？
'''

# -------------------------------------------------------------------------------------------------
#虽然AC不过根本没有效率可言，参考Best Result解法
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums1)):  
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if ans.count(nums1[i]) == min(nums1.count(nums1[i]),nums2.count(nums2[j])):
                        break
                    ans.append(nums1[i])
                    break
        return ([] if (nums1 ==[] and nums2 == []) else ans)


S = Solution()
print(S.intersect([1, 2, 2, 1],[2, 3, 2])) 
print(S.intersect([1, 2, 2, 1],[])) 
print(S.intersect([],[])) 
print(S.intersect([1],[2])) 
print(S.intersect([2],[2])) 
print(S.intersect([1,2,2,1],[2])) 
print(S.intersect([61,24,20,58,95,53,17,32,45,85,70,20,83,62,35,89,5,95,12,86,58,77,30,64,46,13,5,92,67,40,20,38,31,18,89,85,7,30,67,34,62,35,47,98,3,41,53,26,66,40,54,44,57,46,70,60,4,63,82,42,65,59,17,98,29,72,1,96,82,66,98,6,92,31,43,81,88,60,10,55,66,82,0,79,11,81],
[5,25,4,39,57,49,93,79,7,8,49,89,2,7,73,88,45,15,34,92,84,38,85,34,16,6,99,0,2,36,68,52,73,50,77,44,61,48])) 
  
# -------------------------------------------------------------------------------------------------



# -------------------------------------------草稿--------------------------------------------------
# def intersect(nums1, nums2):
#     """
#     :type nums1: List[int]
#     :type nums2: List[int]
#     :rtype: List[int]
#     """
#     ans = []
#     for i in range(len(nums1)):  
#         for j in range(len(nums2)):
#             if nums1[i] == nums2[j]:
#                 if ans.count(nums1[i]) == min(nums1.count(nums1[i]),nums2.count(nums2[j])):
#                     break
#                 ans.append(nums1[i])
#                 break
#     return ([] if (nums1 ==[] and nums2 == []) else ans)
        

# print(intersect([1, 2, 2, 1],[2, 3, 2])) 
# print(intersect([1, 2, 2, 1],[])) 
# print(intersect([],[])) 
# print(intersect([1],[2])) 
# print(intersect([2],[2]))

# from collections import Counter
# def intersect():
#     nums1 = [1, 4, 5, 1]
#     nums2 = [4, 3, 4]
#     c1 = Counter(nums1)
#     c2 = Counter(nums2)

#     for num in c1 & c2:
#         print("num = %s"%num)
#         print([num] * min(c1[num], c2[num]))
    
#      # sum([[num] * min(c1[num], c2[num]) for num in c1 & c2], [])      
# intersect()

# -------------------------------------------------------------------------------------------------


# ----------------------------------------Best Result----------------------------------------------
# from collections import Counter

# class Solution(object):
#     def intersect(self, nums1, nums2):
#         c1, c2 = Counter(nums1), Counter(nums2)
#         return sum([[num] * min(c1[num], c2[num]) for num in c1 & c2], [])

# S = Solution()
# print(S.intersect([1, 2, 2, 1],[2, 3, 2])) 
# print(S.intersect([1, 2, 2, 1],[])) 
# print(S.intersect([],[])) 
# print(S.intersect([1],[2]))        
# -------------------------------------------------------------------------------------------------  

# ----------------------------------------Best Result----------------------------------------------
# def intersect(self, nums1, nums2):
#     a, b = map(collections.Counter, (nums1, nums2))
#     return list((a & b).elements())
# -------------------------------------------------------------------------------------------------  

# ----------------------------------------Best Result----------------------------------------------
# # Variations:

# def intersect(self, nums1, nums2):
#     C = collections.Counter
#     return list((C(nums1) & C(nums2)).elements())
    
# def intersect(self, nums1, nums2):
#     return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())
# -------------------------------------------------------------------------------------------------

# ----------------------------------------Best Result----------------------------------------------

# -------------------------------------------------------------------------------------------------