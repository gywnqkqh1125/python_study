def 둘레(a, b) :
    c = 2 * (a + b)
    return c

def 넓이(d, e) :
    f = d * e
    return f

one = int(input('가로의 길이를 입력하세요. '))
two = int(input('세로의 길이를 입력하세요. '))
print('넓이는 {}, 둘레는 {} 입니다.'.format(넓이(one,two), 둘레(one,two)))