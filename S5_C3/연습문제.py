"""
#1
def hot(drink) :
    print('1. {} 분말을 종이컵에 넣습니다. \n2. 뜨거운 물을 넣습니다.\n3. 섞어줍니다.'.format(drink))
def cool(drink) :
    print('1. {} 시럽을 종이컵에 넣습니다. \n2. 시원한 물을 넣습니다.\n3. 섞어줍니다.'.format(drink))

drink = input('원하는 차를 선택하세요. (코코아/유자차/아이스티/콜라)')
if drink == '코코아' or drink == '유자차' :
    hot(drink)
if drink == '아이스티' or drink == '콜라' :
    cool(drink)
print('{}가 나왔습니다. 맛있게 드세요.'.format(drink))

#2
def exec(counts) :
    #1. 가장 큰 수 찾기
    m = max(counts)
    #2. 가장 작은 수 찾기
    n = min(counts)
    #3. 가장 큰 수와 가장 작은 수의 차 구하기
    return m - n

class1 = [55, 36, 47, 44, 64, 50]
class2 = [58, 39, 63, 50, 46]
class3 = [73, 38, 44, 49, 52, 60]
class4 = [46, 34, 49, 52, 55, 38]

chai = exec(class1)
print('6-1반의 윗몸 일으키기 차이는 {}입니다.'.format(chai))
chai = exec(class2)
print('6-2반의 윗몸 일으키기 차이는 {}입니다.'.format(chai))
chai = exec(class3)
print('6-3반의 윗몸 일으키기 차이는 {}입니다.'.format(chai))
chai = exec(class4)
print('6-4반의 윗몸 일으키기 차이는 {}입니다.'.format(chai))
"""
#3
def bimando(h, w) :
    standard = h/100 * h/100 * 22
    bmi = (w - standard)/standard * 100
    return bmi

num1 = float(input('키를 입력해주세요. '))
num2 = float(input('몸무게를 입력해주세요. '))

bmi = bimando(num1, num2)
print('bmi : {}'.format(bmi))
if bmi < 10 :
    print('비만지수 결과 : 정상입니다.')
elif bmi >= 10 and bmi < 20 :
    print('비만지수 결과 : 과체중')
else :
    print('비만지수 결과 : 비만')