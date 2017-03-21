'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

'''


# ------------------------------------------------------------------------------
# ☆经典题目
#注意：
#分清楚概念，linear时间复杂度并不代表不能用for循环，此处的for实际上也是遍历一次的异或循环
# ------------------------------------------------------------------------------
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        res = 0
        for i in nums:
            res ^= i
        return res

S = Solution()
print(S.singleNumber([1,1,2,3,3]))




# ------------------------------------Best Resule------------------------------------------
# from functools import reduce
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # return reduce(operator.xor, nums)
#         return reduce(lambda x, y: x^y, nums) 

        
#         res = 0
#         for i in nums:
#             res ^= i
#         return res

# S = Solution()
# print(S.singleNumber([1,1,2,3,3]))
# ------------------------------------------------------------------------------




# ----------------------------------草稿--------------------------------------------
# ret = set(range(1, len(nums)+1))
# ret = ret - set(nums)
# test = [1,1,2,3,3]

# print()
# ------------------------------------------------------------------------------        