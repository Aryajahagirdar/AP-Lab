def functionOne():
    pass

def functionTwo():
    a = 1

def functionThree(a):
    b = 1
    return a+b

print('Number of local variables in first function is:', functionOne.__code__.co_nlocals)
print('Number of local variables in second function is:', functionTwo.__code__.co_nlocals)
print('Number of local variables in third function is:', functionThree.__code__.co_nlocals)
