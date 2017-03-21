'''
Given two strings s and t, write a function to determine if t is an anagram(n· 由颠倒字母顺序而构成的字[短语]) of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

# -------------------------------------------------------------------------------------------------
# 
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

S = Solution()

print(S.isAnagram("aaa","a"))        
# -------------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------------
# def isAnagram(s, t):
#     """
#     :type s: str
#     :type t: str
#     :rtype: bool
#     """
#     if set(list(s))-set(list(t)) == set():
#         print (True)
#     else:
#         print (False)
    
#     # print(set(list(s))-set(list(t)))

# isAnagram("aaa","aaaa")
# -------------------------------------------------------------------------------------------------