def sum_num(n,m):
    total=0
    for i in range(n,m+1):
        total=total+i
    return total

answer=sum_num(1,10)
print('1부터 10까지의 합: {}'.format(answer))

answer=sum_num(5,10)
print('5부터 10까지의 합: {}'.format(answer))