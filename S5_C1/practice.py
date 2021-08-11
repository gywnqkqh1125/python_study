#1
"""
def 넓이(n) :
    res = n * n
    return res

def 둘레(n) :
    res = n * 4
    return res

n = int(input('정사각형의 한 변의 길이를 입력해주세요.: '))
print('이 정사각형의 넓이는 {}입니다.'.format(넓이(n)))
print('이 정사각형의 둘레는 {}입니다.'.format(둘레(n)))

#2
def 겉넓이(n1, n2, n3) :
    res = (n1*n2 + n2*n3 + n3*n1) * 2
    return res

def 부피(n1, n2, n3) :
    res = n1 * n2 * n3
    return res

n1 = int(input('직육면체 가로의 길이를 입력해주세요.: '))
n2 = int(input('직육면체 세로의 길이를 입력해주세요.: '))
n3 = int(input('직육면체 높이의 길이를 입력해주세요.: '))

print('이 직육면체의 겉넓이는 {}입니다.'.format(겉넓이(n1, n2, n3)))
print('이 직육면체의 부피는 {}입니다.'.format(부피(n1, n2, n3)))

#3
def type01(a, b, c) :
    res = a * b - c
    return res

def type02(a, b, c) :
    res = a + b * c
    return res

def type03(a, b, c) :
    res = a / b + c
    return res

typeInput = int(input('유형을 선택해주세요.(1, 2, 3) '))
result = 0
num1 = int(input('첫 번째 숫자를 입력해주세요. '))
num2 = int(input('두 번째 숫자를 입력해주세요. '))
num3 = int(input('세 번째 숫자를 입력해주세요. '))

if typeInput == 1 :
    result = type01(num1, num2, num3)
elif typeInput == 2 :
    result = type02(num1, num2, num3)
elif typeInput == 3 :
    result = type03(num1, num2, num3)

print('계산결과는 {}입니다.'.format(result))
"""
#4
import time

def add(a, b) :
    res = a + b
    return res
def minus(a, b) :
    res = a - b
    return res
def multi(a, b) :
    res = a * b
    return res
def div(a, b) :
    res = a / b
    return res
def tria(a, b) :
    res = a * b / 2
    return res
def square(a, b) :
    res = (a + b) * 2
    return res

while True :
    print('어떤 계산을 하고 싶은지 골라주세요.')
    n = int(input(' 더하기(1) \n 빼기(2) \n 곱하기(3) \n 나누기(4) \n 삼각형의 넓이(5) \n 직사각형의 둘레 \n 종료(0) \n 입력: '))
    if n == 0 :
        break
    a = int(input('첫 번째 숫자를 입력해주세요. '))
    b = int(input('두 번째 숫자를 입력해주세요. '))
    if n == 1 :
        result = add(a, b)
    elif n == 2 :
        result = minus(a, b)
    elif n == 3 :
        result = multi(a, b)
    elif n == 4 :
        result = div(a, b)
    elif n == 5 :
        result = tria(a, b)
    elif n == 6 :
        result = square(a, b)

    print('계산결과는 {}입니다.'.format(result))
    print('_______________________')
    time.sleep(3)