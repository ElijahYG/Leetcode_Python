# ------------------------------------------------------------------------------------------------------------
'''
258. Add Digits-迭代
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime? 
'''
# ------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------
# 这是一个经典的Digit Root 问题
# https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
# -----------------------------------------------------------------------

class Solution(object):
    
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        elif (num % 9) == 0:
        	return 9
       	else:
            return num % 9


S = Solution()
print(S.addDigits(17)) 




# -------------------------------------Method 2--------------------------------------------------
# class Solution(object):
#     def addDigits(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         if num == 0:
#             return 0
#         else:
#             return 1 + (num - 1) % 9
# ----------------------------------------------------------------------------------------------      


# -------------------------------------Method 2--------------------------------------------------
# class Solution(object):
    
#     def addDigits(self, num):
#         if num>=10:
#             re=num%10
#             qu=(num-re)/10
#             new_num=re+qu
#             return self.addDigits(new_num)
#         else:
#             return num 
# ----------------------------------------------------------------------------------------------   










# import math
# a = 12345
# # b = a % 10
# b = (math.floor(a / 10)) % 10
# # b = (a / 100) % 10
# print(len(str(a)))