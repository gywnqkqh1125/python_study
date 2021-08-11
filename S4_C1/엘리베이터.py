import random

num = int(input('몇 층에 가실 건가요? '))
print('이 엘리베이터의 정원은 8명입니다.')

people = random.randint(1,12)
print(people,'명이 탑승했습니다.')

if people > 8:
    print('현재 {}명이 탑승했습니다.'.format(people))
    print('정원초과입니다. {}명 내려주세요'.format(people-8))
else:
    for i in range(1,num):
        print(i,'층.')
    print(num,'층. 문이 열립니다.')