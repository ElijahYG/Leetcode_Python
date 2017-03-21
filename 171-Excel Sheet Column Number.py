'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''

# -------------------------------------------------------------------------------------------------
# 
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        res = 0
        box = {'A':1 ,'B':2 ,'C':3 ,'D':4 ,'E':5 ,'F':6 ,'G':7 ,'H':8 ,'I':9 ,'J':10 ,'K':11 ,'L':12 ,'M':13 ,'N':14 ,'O':15 ,
           'P':16 ,'Q':17 ,'R':18 ,'S':19 ,'T':20 ,'U':21 ,'V':22 ,'W':23 ,'X':24 ,'Y':25 ,'Z':26}
        for i in s:
            res = box[i] * (26**((len(s)-1)-count)) + res
            count += 1
        return res
         

S = Solution()
print(S.titleToNumber("BBA"))        
# -------------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------------
# len(s)-1)-s.index(i)中s.index(i)处，如果出现"BB"这种情况，就会出现总会找第一个B的位置，所得结果会大
# def titleToNumber(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     res = 0
#     box = {'A':1 ,'B':2 ,'C':3 ,'D':4 ,'E':5 ,'F':6 ,'G':7 ,'H':8 ,'I':9 ,'J':10 ,'K':11 ,'L':12 ,'M':13 ,'N':14 ,'O':15 ,
#            'P':16 ,'Q':17 ,'R':18 ,'S':19 ,'T':20 ,'U':21 ,'V':22 ,'W':23 ,'X':24 ,'Y':25 ,'Z':26}
#     # print(box['Z'])
#     for i in s:
#         res = box[i] * (26**((len(s)-1)-s.index(i))) + res
#         print('box[%s] = %s'%(i,box[i]))
#         # print('len(s) = %s'%len(s))
#         # print('s.index(%s) = %s'%(i,(s.index(i))))
#         print('(len(s)-1)-s.index(%s)) = %s'%(i,(len(s)-1)-s.index(i)))

#     print('res = %s'%res)         

# titleToNumber('BB')
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# 最终版本
# def titleToNumber(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     res = 0
#     count = 0
#     box = {'A':1 ,'B':2 ,'C':3 ,'D':4 ,'E':5 ,'F':6 ,'G':7 ,'H':8 ,'I':9 ,'J':10 ,'K':11 ,'L':12 ,'M':13 ,'N':14 ,'O':15 ,
#            'P':16 ,'Q':17 ,'R':18 ,'S':19 ,'T':20 ,'U':21 ,'V':22 ,'W':23 ,'X':24 ,'Y':25 ,'Z':26}
#     # print(box['Z'])
#     for i in s:

#         res = box[i] * (26**((len(s)-1)-count)) + res
#         count += 1
#         print('box[%s] = %s'%(i,box[i]))
#         # print('len(s) = %s'%len(s))
#         # print('s.index(%s) = %s'%(i,(s.index(i))))
#         print('(len(s)-1)-s.index(%s)) = %s'%(i,(len(s)-1)-s.index(i)))

#     print('res = %s'%res)         

# titleToNumber('')
# -------------------------------------------------------------------------------------------------

# -----------------------------------Best Result---------------------------------------------------
# return reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)]) 
# -------------------------------------------------------------------------------------------------

# -----------------------------------Best Result---------------------------------------------------
# return reduce(lambda x,y:x*26+y,map(lambda x:ord(x)-ord('A')+1,s))
# -------------------------------------------------------------------------------------------------