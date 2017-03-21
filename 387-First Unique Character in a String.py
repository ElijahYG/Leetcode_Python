'''
 Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters. 
'''

# -------------------------------------------------------------------------------------------------
# 用以下方法，时间复杂度太高 Time Limit Exceeded，不符合要求
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in s:
            if (collections.Counter(s))[i] == 1:
                return (s.find(i)) 
            # print((collections.Counter(s))[i])
        return -1
S = Solution()
print(S.firstUniqChar("leetcode"))
print(S.firstUniqChar("leetcodeleetcode"))
print(S.firstUniqChar("loveleetcode"))     
print(S.firstUniqChar(""))
# -------------------------------------------------------------------------------------------------



# --------------------------------------------草稿-------------------------------------------------
# import collections
# def firstUniqChar(s):
#     for i in s:
#         if (collections.Counter(s))[i] == 1:
#             return (s.find(i)) 
#     # print(s.find('b'))
# firstUniqChar('aabbccdefa')

# -------------------------------------------------------------------------------------------------

# -----------------------------------------AC Method--------------------------------------------
def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
    letters='abcdefghijklmnopqrstuvwxyz'
    index=[s.index(l) for l in letters if s.count(l) == 1]
    return min(index) if len(index) > 0 else -1
# -------------------------------------------------------------------------------------------------
# -----------------------------------------Other Method--------------------------------------------
# 用以下方法，时间复杂度太高 Time Limit Exceeded，不符合要求
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            c = s[i]
            if s.count(c)==1:
                return i
        return -1
# -------------------------------------------------------------------------------------------------
# -----------------------------------------Other Method--------------------------------------------
    def firstUniqChar2(self, s):

        from collections import Counter
        sc = Counter(s)
        for i in range(len(s)):
            c = s[i]
            if sc.get(c,0)==1:
                return i

        return -1
# -------------------------------------------------------------------------------------------------
# -----------------------------------------Other Method--------------------------------------------
    def firstUniqChar3(self, s):

        d = {}
        for c in s:
            if c in d.keys():
                d[c] += 1
            else:
                d[c] = 1

        for i in range(len(s)):
            c = s[i]
            if d[c]==1:
                return i

        return -1 
# -------------------------------------------------------------------------------------------------