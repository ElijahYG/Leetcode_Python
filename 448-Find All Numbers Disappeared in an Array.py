'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''

# ------------------------------------------------------------------------------
#Best Result ：此题自己没有AC，标记
# ------------------------------------------------------------------------------
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = set(range(1, len(nums)+1))
        ret = ret - set(nums)
        return list(ret) 


S = Solution()
print(S.findDisappearedNumbers([1,2,2,9,4,7,6,6,5]))
print(S.findDisappearedNumbers([]))      
print(S.findDisappearedNumbers([1,1]))   
# ------------------------------------------------------------------------------






# ------------------------------------------------------------------------------
#以下方法可以正常执行，但是时间不合要求TLE(Time Limit Exceeded),
# ------------------------------------------------------------------------------
# class Solution(object):
#     def findDisappearedNumbers(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         res = []
#         for x in range(len(nums)):
#             if (x+1) not in nums:
#             	res.append(x+1)
#         return res    

# S = Solution()
# print(S.findDisappearedNumbers([1,2,2,9,4,7,6,6,5]))
# print(S.findDisappearedNumbers([]))      
# print(S.findDisappearedNumbers([1,1]))   
# ------------------------------------------------------------------------------



# array = [1,2,3,2]
# print(min(array))
# for x in range(max(array)):
#     print('x=%s'%x)
# else:
#     print('NO')	
# print(array.index(2))


