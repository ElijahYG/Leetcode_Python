map([1,2,3], f) -> [f(1), f(2), f(3)]
def map(lst,f):
    ans = []
    for i in lst:
        ans.append(f(i))
    return ans
    

reduce（lst，f， init） - [1,2,3] lambda x, y: x + y 0
-> f(f(f(0, 1), 2), 3)
   def reduce(lst,f,init):
       # init = 
       for i in range(lst):
           init = f(init, lst[i])
       return init     
       
       
   def reduce(lst, f, init):
       if len(lst) == 0:
           return init
       return reduce(lst[1:], f, f(init, lst[0]))



