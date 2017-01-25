#Who likes it?

def likes(names):
    #your code here
    if (len(names) < 1):
        return 'no one likes this'
    elif (len(names) == 1):
        a = (names[0])
        b = ' likes this'
        c = a + b
        return c
    elif (len(names) == 2):
        a = (names[0] + ' and ' + names[1])
        b = ' like this'
        c = a + b
        return c
    elif (len(names) == 3):
        a = (names[0] + ',' + names[1] + ' and ' + names[2])
        b = ' like this'
        c = a + b
        return c        
    else:
        a = (names[0] + ',' + names[1])
        b = ' and ' + str(len(names) - 2) + ' others likes this'
        c = a + b
        return c





print(likes(['Alex', 'Jacob', 'Mark', 'Max']))




# names = ['Max']

# print(type(len(names)))



