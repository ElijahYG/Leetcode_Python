'''
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

# -------------------------------------------------------------------------------------------------
# 
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        score = 0
        for i in set(nums):
            if (nums.count(i) > score):
                score = nums.count(i)
                res = i 
        return (res)


S = Solution()

print(S.majorityElement([1,1,1,1,1,3,3,3,3,3,35,7,5,5,5,5,8,8,8,8,8,8]))        
# -------------------------------------------------------------------------------------------------



# -------------------------------------------草稿--------------------------------------------------
# def majorityElement():
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     # nums = [1,1,1,1,1,3,3,3,3,3,35,7,5,5,5,5,8,8,8,8,8,8]
#     nums = [1,1,1,1,1,3,3,3,3,3,35,7,5,5,5,5,8,8,8,8,8,8,56,756,7,567,567,56,75,7,567,567,56,7,567,567,3,3,3,3,3,3,3,3,3,33,1,1,1,5,5,5,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,456,45,64,64,564,64,564,64,6,46,46,54]
#     res = 0
#     score = 0
#     for i in set(nums):
#         if (nums.count(i) > score):
#            print('外面的nums.count(%s) = %s'%(i,nums.count(i)))
#            print('外面的score = %s'%score)
#            score = nums.count(i)
#            res = i 
#            print('赋值后的nums.count(%s) = %s'%(i,nums.count(i)))
#            print('赋值后的score = %s'%score)
#     print (res)    
        
# majorityElement()
# -------------------------------------------------------------------------------------------------

# ----------------------------------------Best Result----------------------------------------------
#NOTICE that the majority element always exist in the array,so that the middle always is the answer
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(num)[len(num)/2]
# -------------------------------------------------------------------------------------------------        
