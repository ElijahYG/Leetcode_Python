class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        s = nums[ : ]
        while i < (s.count(0)):
            nums.remove(0)
            nums.append(0)
            i+=1 
        print(nums)

S = Solution()
S.moveZeroes([0,1,0,3,12,0,100,99,0,87])




# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         i = 0
#         s = nums[ : ]
#         nums = list(set(nums))
#         nums.remove(0)
#         print('nums=%s'%nums)
#         while i < (s.count(0)):
#             nums.append(0)
#             i+=1
        

# nums = [0,1,0,3,12]
# Solution(nums)



# a = [1,1,1,0,4,0,0,2,3,0]
# b = list(set(a))
# b.remove(0)

# print(b)
# print(len(a))

