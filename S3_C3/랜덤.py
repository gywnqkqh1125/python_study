import random

input('부루마블 게임입니다! 엔터키를 눌러 주사위를 던지세요.')
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

print('첫 번째 주사위 : %d칸' %dice1)
print('두 번째 주사위 : %d칸' %dice2)
dice = dice1 + dice2
print('%d칸 이동하세요.' %dice)