def cal(*nums) :
    total = 0
    for n in nums :
        total = total + n
    return total

print(cal(2,4,6,8,10,12,14,16,18,20,90))