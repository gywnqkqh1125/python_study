def calc(name, num) :
    print('입력한 버거: {}, 개수: {}'.format(name, num))
    if name == 'a' :
        result = 2000 * num
        print('불고기버거를 {}개 주문하셨습니다.'.format(num))
    if name == 'b' :
        result = 1800 * num
        print('치즈버거를 {}개 주문하셨습니다.'.format(num))
    if name == 'c' :
        result = 2400 * num
        print('새우버거를 {}개 주문하셨습니다.'.format(num))
    return result

print('어떤 햄버거를 주문하시겠어요?')
print('\t [메뉴] ')
print('\t a: 불고기버거(2000원)')
print('\t b: 치즈버거(1800원)')
print('\t c: 새우버거(2400원)')
burger = input('입력: ')
n = int(input('원하시는 개수를 입력해주세요. '))

total = calc(burger, n)
print('금액은 총 {}원입니다.'.format(total))