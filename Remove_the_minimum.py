# -------------------------------------------------
# The museum of incredible dull things
# The museum of incredible dull things wants to get rid of some exhibitions. Miriam, the interior architect, comes up with a plan to remove the most boring exhibitions. She gives them a rating, and then removes the one with the lowest rating.
# However, just as she finished rating all exhibitions, she's off to an important fair, so she asks you to write a program that tells her the ratings of the items after one removed the lowest one. Fair enough.

# Task
# Given an array of integers, remove the smallest value. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.
# Don't change the order of the elements that are left.

# Examples

# remove_smallest([1,2,3,4,5]) = [2,3,4,5]
# remove_smallest([5,3,2,1,4]) = [5,3,2,4]
# remove_smallest([2,2,1,2,1]) = [2,2,2,1]
# -------------------------------------------------

def remove_smallest(numbers):
    try:
        s = numbers[ : ]
        s.sort()
        numbers.remove(s[0])
        return numbers
    except Exception:
        return []



print(remove_smallest([])) 
#[2,3,4,5]    


# ---------------------Best Result-----------------------
# def remove_smallest(numbers):
#     if numbers:
#         numbers.remove(min(numbers))
#     return numbers
# -------------------------------------------------------

# ---------------------Best Result-----------------------
# def remove_smallest(a):
#     if len(a) > 0 :
#         a.remove(min(a))
#     return a
# -------------------------------------------------------






# numbers = [1,3,2,5,4]
# s = numbers[ : ]
# s.sort()
# numbers.remove(s[0])





# --------------------------------------------------------
# 如果需要一个排序好的副本，同时保持原有列表不变，怎么实现呢?
# x =[4, 6, 2, 1, 7, 9]
# y = x[ : ]
# y.sort()
# print y #[1, 2, 4, 6, 7, 9]
# print x #[4, 6, 2, 1, 7, 9]
# --------------------------------------------------------
