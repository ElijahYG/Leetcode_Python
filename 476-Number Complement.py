'''
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:

    1.The given integer is guaranteed to fit within the range of a 32-bit signed integer.
    2.You could assume no leading zero bit in the integer’s binary representation.

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

'''
'''
给定一个正整数，输出其补数。 补码策略是翻转其二进制表示的比特。

注意：

     1、给定的整数保证适合在32位有符号整数的范围内。
     2、您可以假设整数的二进制表示法中没有前导零位。
'''

# ---------------------------------------------------------------------------------------------------
# 思路：
# 1、32位有符号整数的范围：-2^31~2^31-1
# 2、原码：一个正数，按照绝对值大小转换成的二进制数；一个负数按照绝对值大小转换成的二进制数，然后最高位补1，称为原码。 
# 	 反码：正数的反码与原码相同，负数的反码为对该数的原码除符号位外各位取反。 
# 	 补码：正数的补码与原码相同，负数的补码为对该数的原码除符号位外各位取反，然后在最后一位加1. 
# ---------------------------------------------------------------------------------------------------

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        if '-' in str(num):
            cplmt = bin(num).replace('-0b','1')
        else:
            cplmt = bin(num).replace('0b','')
        ls = []
        for x in range(len(cplmt)):
            ls.append('1')
        true = int(''.join(ls))
        ret = true - int(cplmt)
        
        ret_list = str(ret) 
        
        # print('ret=%s'%ret)
        res = int(ret_list,base=2)
        return res

S = Solution()
print(S.findComplement(-22))


# ---------------------------------草稿--------------------------------------------------------------
# number = 22
# buma = bin(number).replace('0b','')
# ls = []
# for x in range(len(buma)):
#     ls.append('1')
# print(int(''.join(ls)))
# 
# yuanma = 11111
# ret = yuanma - int(buma)
# print('buma=%s'%buma)
# print('ret=%s'%ret)

