'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

PS·palindromes——回文是对称的字符串或者对称的数字是数字,如level和123321都是回文

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

# -------------------------------------------------------------------------------------------------
'''
解题思路：
统计每个字母的出现次数：
若字母出现偶数次，则直接累加至最终结果
若字母出现奇数次，则将其值-1之后累加至最终结果
若存在出现奇数次的字母，将最终结果+1
'''
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = odd = 0
        cnt = collections.Counter(s)
        for c in cnt:
            ans += cnt[c]
            if cnt[c] % 2 == 1:
                ans -= 1
                odd += 1
        return (ans + (odd > 0))

S = Solution()
print(S.longestPalindrome("aaabbbccccdd"))   
# -------------------------------------------------------------------------------------------------



# -------------------------------------------草稿--------------------------------------------------
# import collections
# def longestPalindrome():
#     """
#     :type s: str
#     :rtype: int
#     """
#     s = "aaabbbccccdd" 
#     ans = odd = 0
#     cnt = collections.Counter(s)
#     print('cnt = %s'%cnt)
#     for c in cnt:
#         print('cnt[c] = %s'%cnt[c])
#         ans += cnt[c]
#         print('c = %s ,ans = %s'%(c,ans))
#         if cnt[c] % 2 == 1:
#             ans -= 1
#             odd += 1
#     print (ans + (odd > 0))
# longestPalindrome()
# -------------------------------------------------------------------------------------------------

# ----------------------------------------Best Result----------------------------------------------
#很有参考意义：collections.Counter(s).values()
# def longestPalindrome(self, s):
#     odds = sum(v & 1 for v in collections.Counter(s).values())
#     return len(s) - odds + bool(odds)
# -------------------------------------------------------------------------------------------------        
