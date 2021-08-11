"""
#1-1
a=1
while a<11:
    print(a)
    a=a+1
#1-2
a=int(input('숫자를 입력해주세요. '))
i=1
while i<a+1:
    print(i)
    i=i+1
#1-3
i=40
while i<=70:
    if i%2!=0:
        print(i)
    i=i+1
#1-4
i=-30
while i>-80:
    if i%2==0:
        print(i)
    i=i-1

#2
total=0
num1=int(input('시작할 수를 입력해주세요. '))
num2=int(input('끝나는 수를 입력해주세요. '))
while num1!=num2+1:
    total=total+num1
    num1=num1+1
print('답은 {}입니다.'.format(total))

#3
import random as rand
answer=rand.randint(1,6)
num=int(input('주사위를 던져서 나온 숫자를 맞혀주세요 '))
cnt=1
while num!=answer:
    print('틀렷습니다. 다시 맞혀주세요.')
    num=int(input('주사위를 던져서 나온 숫자를 맞혀주세요 '))
    cnt=cnt+1
print('정답입니다. {}번 만에 맞혔습니다.'.format(cnt))
"""
import time
degree=int(input('몇 도까지 끓이실 건가요? '))
water=0
while water!=degree:
    print('현재 온도는 {}도 입니다.'.format(water))
    water=water+10
    time.sleep(1)
print('{}도 입니다. 다 끓었습니다.'.format(water))