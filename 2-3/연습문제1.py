"""

#1
a = 182 + 13
b = 5312 / 14
c = 12 * 11
d = (176 - 21) / 2
e = 832 - 519
f = 192

print('%.1f' % max(a, b, c, d, e, f))
print(min(a, b, c, d, e, f))

#3
print('더치페이 계산기')
total = int(input('내야할 금액은 얼마인가요?'))
people = int(input('사람은 몇 명인가요?'))

result = total // people
print('1인당 낼 돈 : %d' % result)

mod = total % people
print('부족한 돈 : %d' % mod)

#4
print('자동차 유류비 계산기')
distance = int(input('운행 거리를 입력해주세요.(단위 : km.) '))
y = float(input('차량의 연비를 입력해주세요.(단위 : km/l) '))
oil = int(input('기름의 가격을 입력해주세요.(단위 : 원/l) '))
l = round(distance / y, 1)
w = l * oil

print('예상 필요 주유량은 %.f리터 입니다.' %l)
print('예산 주유 비용은 %.d원 입니다.' %int(w))

#5
total = 48
T = 7
B = 3

numT = total // T
numB = (total - (T * numT)) // B

print('트와이스 노래 : ', numT, '곡')
print('블랙핑크 노래 : ', numB, '곡')
"""
#6
kim = 72+63+82+49+91+75
lee = 58+72+47+92+87+82
park = 83+81+29+56+92+69
hwang = 63+49+86+37+85+64
ou = 72+58+62+59+82+79

kim = kim / 6
lee = lee / 6
park = park / 6
hwang = hwang / 6
ou = ou / 6

result1 = max(kim, lee, park, hwang, ou)
result2 = min(kim, lee, park, hwang, ou)
result3 = abs(result1 - result2)

print('1등의 평균 점수는 %.f점 입니다.' %result1)
print('5등의 평균 점수는 %.f점 입니다.' %result2)
print('1등과 5등의 점수 차이는 %.f점 입니다.' %result3)