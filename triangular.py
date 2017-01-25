def triangular(n):
    #your code here
    if n < 0:
        return 0
    else:
        score = (n*(n+1))/2
    return score



print(triangular(-9))    