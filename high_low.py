def high_and_low(numbers):
    try:
        high_num = low_num = int(numbers[0:(numbers.index(' '))])
    except Exception:
        high_num = low_num = int(numbers[0:]) 
    for num in numbers.split(' '):
        if int(num) > high_num:
            high_num = int(num)
        if int(num) < low_num:
            low_num = int(num)   
    score = (str(high_num)+' '+str(low_num))
    return score

print (high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
print (high_and_low("42"))



# ---------------------Best Result------------------------------
# def high_and_low(numbers): #z.
#    nn = [int(s) for s in numbers.split(" ")]
#    return "%i %i" % (max(nn),min(nn))
# --------------------------------------------------------------
# 
# ---------------------Best Result------------------------------
# def high_and_low(numbers):
#   n = map(int, numbers.split(' '))
#   return str(max(n)) + ' ' + str(min(n))
# --------------------------------------------------------------
# 
# ---------------------Best Result------------------------------
# def high_and_low(numbers):
#     nums = sorted(numbers.split(), key=int)
#     return '{} {}'.format(nums[-1], nums[0])
# --------------------------------------------------------------



# ------------------分离空格-------------------------
# s ="4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"
# x = s.split(' ')  
# y = ''.join(x)  
# print(y)
# ---------------------------------------------------

# info = '-12'
# try:
#     print(info.index(' '))
# except Exception:
#     print(info)

