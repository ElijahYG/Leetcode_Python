'''
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, 
where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
'''

# ---------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------

# class Solution(object):
#     def minMoves(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()
#         if len(set(nums)) == 1:
#             return nums
#         for x in range(len(nums)):
#             nums[x] += 1
#         return (self.minMoves(nums)) 	




# S = Solution()
# print(S.minMoves([1,2,3]))
# ---------------------------------------------------------------------------------------------------




# ---------------------------------------------------------------------------------------------------
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while len(set(nums)) != 1:
            if i < (len(nums)-1):
                nums[i] += 1
                i += 1
        return nums

            
           




S = Solution()
# print(S.minMoves([1,2,3]))
# print(S.minMoves([2,5,7]))
print(S.minMoves([1,3,6,12]))

# #判断所有元素值是否一致
# a= [2,2,2]
# print(len(set(a)))

# ---------------------------------------------------------------------------------------------------