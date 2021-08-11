import random
"""
#1
내선택 = input('무엇을 내실 건가요?(가위/바위/보) ')
컴퓨터선택 = random.choice(['가위', '바위', '보'])

print('컴퓨터는 {}(을)를 냈습니다.'.format(컴퓨터선택))

if (내선택 == '가위' and 컴퓨터선택 == '보') or (내선택 == '바위' and 컴퓨터선택 == '가위') or (내선택 == '보' and 컴퓨터선택 == '바위') :
    print('컴퓨터가 졌어요.')
if (내선택 == '가위' and 컴퓨터선택 == '바위') or (내선택 == '바위' and 컴퓨터선택 == '보') or (내선택 == '보' and 컴퓨터선택 == '가위') :
    print('컴퓨터가 이겼어요.')
if (내선택 == '가위' and 컴퓨터선택 == '가위') or (내선택 == '바위' and 컴퓨터선택 == '바위') or (내선택 == '보' and 컴퓨터선택 == '보') :
    print('비겼어요.')

#2
score = int(input('점수를 입력하세요. '))

print('{}점 입니다.'.format(score))

grade = 0
if score >= 90 :
    grade = 1
elif score >= 80 :
    grade = 2
elif score >= 70 :
    grade = 3
elif score >= 60 :
    grade = 4
else :
    grade = 5

print('{}등급입니다.'.format(grade))

#3
print('구구단 테스트')

num1 = random.randint(2, 9)
num2 = random.randint(1, 9)

답변 = int(input('{} * {} = '.format(num1, num2)))
정답 = num1 * num2

if 답변 == 정답 :
    print('맞았습니다.')
else :
    print('틀렸습니다.')
"""
print('안녕하세요. 댄스 동아리 가입을 위해 몇 가지 확인하도록 하겠습니다.')

질문1 = input('당신의 성별을 무엇입니까? (남/여) ')
질문2 = int(input('당신은 몇 살입니까? '))
질문3 = input('댄스대회 입상 경험이 있습니까? (예/아니오) ')
result = 0

if 질문1 == '여' :
    if 질문2 < 12 :
        if 질문3 == '예' :
            result = 1
        else :
            result = 2
        if 질문2 > 13 :
            result = 2
    else :
        result = 1
else :
    result = 2

if result == 1 :
    print('동아리에 가입되었습니다. 환영합니다.')
else :
    print('동아리 가입이 불가능합니다.')