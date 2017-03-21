'''
 Given an arbitrary ransom note string and another string containing letters from all the magazines, 
 write a function that will return true if the ransom note can be constructed from the magazines ; 
 otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

# ------------------------------------------------------------------------------------------------------
# 注意事项：
# 如果直接用字符串的循环，那么测试数据的第一条是错误的，因为a在ab中都是存在的，但是a有两个，不能进行区分
# ------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------
import collections 
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return not collections.Counter(ransomNote) - collections.Counter(magazine)


S = Solution()
print(S.canConstruct('aa','ab'))
print(S.canConstruct('a','b'))
print(S.canConstruct('a','ba'))

# ------------------------------------------------------------------------------------------------------

# ---------------------------------------Best Result----------------------------------------------------
#O(m+n) with m and n being the lengths of the strings.
# import collections 
# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         return not collections.Counter(ransomNote) - collections.Counter(magazine)

# S = Solution()
# print(S.canConstruct('aa','ab'))
# ------------------------------------------------------------------------------------------------------


# -------------------------------------------草稿-------------------------------------------------------
# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """

# S = Solution()
# print(S.canConstruct('a','b'))
# print(S.canConstruct('a','ba'))

# ------------------------------------------------------------------------------------------------------