import random as rand
num=rand.randint(1,100)

answer=0
count=0

while answer!=num:
    answer=int(input('숫자를 맞혀주세요. '))
    count=count+1
    if answer<num:
        print('Up!')
    elif answer>num:
        print('Down!')

print('정답입니다.')
print('{}번 만에 맞혔습니다.'.format(count))