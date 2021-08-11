import random as ran

def dice() :
    return ran.randint(1,6)

print('내가 굴린 주사위의 눈 : {}'.format(dice()))
print('컴퓨터가 굴린 주사위의 눈 : {}'.format(dice()))