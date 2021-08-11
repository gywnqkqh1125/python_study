"""
for i in range(0, 4, 1):
    print('{}번째 안녕'.format(i))
print('')
for i in range(4, 0, -1):
    print('{}번째 안녕'.format(i))
print('')
for i in range(5):
    print('안녕')

total = 0
for i in range(1,11,1):
    total = total + i
print('1부터 10까지의 합게는 {}입니다.'.format(total))
"""
a = 0
for i in "동해물과 백두산이 마르고 닳도록 하느님이 보우하사":
    a = a + 1
    if i == '하':
        print(a)