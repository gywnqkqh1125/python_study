a = 1
def j() :
    a = 10
    return a

print(j())
print(a)

a = 1
def j() :
    global a
    a = 10
    return a

print(j())
print(a)