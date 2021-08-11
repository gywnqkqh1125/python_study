n = int(input('수를 입력해주세요. '))

if n % 2 == 0 and n % 3 == 0 :
    print('{}은/는 2와 3의 공베수입니다.'.format(n))
else :
    print('{}은/는 2와 3의 공베수가 아닙니다.'.format(n))