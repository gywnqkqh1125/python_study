def 수의합(first, second) :
    res = 0
    for i in range(first, second+1) :
        res = res + i
    return res

print(수의합(1, 10))
print(수의합(1, 100))
print(수의합(1, 1000))