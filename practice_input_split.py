"""
a, b, c = map(int, input('숫자 세 개를 입력하세요.').split())
print(a+b+c)

age, sungjuk = map(int, input('나이와 성적을 순서대로 입력하세요.').split())
print(age, sungjuk)
"""

w, h = map(float, input('몸무게와 키를 순서대로 입력하세요.').split(','))
result = w / (h ** 2) * 10000
print('몸무게: ', w, '키: ', h)
print('체질량지수: %.1f' %result)