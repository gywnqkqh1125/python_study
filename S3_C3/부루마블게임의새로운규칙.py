import random

print('부루마블 게임')
input('엔터키를 눌러 주사위를 던지세요.')
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
result = 0

print('첫 번째 주사위 : {}칸'.format(dice1))
print('두 번째 주사위 : {}칸'.format(dice2))

if (dice1 % 3 == 0) and (dice2 % 3 == 0) :
    if dice1 == dice2 :
        result = (dice1 + dice2) * 4
    else :
        result = (dice1 + dice2) * 3
elif dice1 == dice2 :
    result = (dice1 + dice2) * 2
else :
    result = dice1 + dice2

print('{}칸 이동하세요.'.format(result))