# ------------------------------------------------------
'''
Two to One 

Description:
Take 2 strings s1 and s2 including only letters from ato z. 
Return a new sorted string, the longest possible, containing distinct letters, - each taken only once - coming from s1 or s2.

Examples:

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
'''

#------------------------------------------------------

def longest(s1, s2):     
    s3 = s1 + s2
    s = list(s3)
    s.sort() 
    for i in s:  
        while s.count(i) > 1:  
            s.remove(i)  
    s = "".join(s) 
    return s  
  
print(longest("aretheyhere", "yestheyarehere")) 


# -------------------Best Result-------------------------
#def longest(a1, a2):
#    return "".join(sorted(set(a1 + a2)))
# -------------------------------------------------------


# -------------------------------------------------------
# s = "string"    #字符串
# l = list(s)     #把字符串s改成列表
# l.sort()	    #将列表l排序-按字母顺序
# s = "".join(l)  #再把列表导入至字符串，最后打印输出

# print("l =%s"%l)
# print(s)
# -------------------------------------------------------

# -------------------------------------------------------
# def longest(s1, s2):
#     # your code
#     s3 = s1 + s2
#     s = list(s3)
#     s.sort()
# 	for i in s:  
#         while s.count(i) > 1:  
#         	s.remove(i)  
#      sn = "".join(s)
#      return sn  

# print(longest("aretheyhere", "yestheyarehere")) 
# print(longest("acd", "bef")) 

#aehrsty
#aaeeeeeeeeehhhhrrrrsttyyy
# -------------------------------------------------------






