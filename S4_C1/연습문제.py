"""
#1-1
for i in range(1,11):
    print(i)
#1-2
num = int(input('숫자를 입력해주세요'))
for i in range(1, num+1):
    print(i)
#1-3
for i in range(20,30):
    if i % 2 == 1:
        print(i)
for i in range(21,30,2):
    print(i)
#1-4
for i in range(-10,-40,-1):
    if i % 3 == 0:
        print(i)

#2
소나기 = '글쎄 말이지. 이번 앤 꽤 여러 날 앓는 걸 약도 변변히 못서 봤다더군. 지금 같아서 윤초시네도 대가 끊긴 셈이지...그런데 참, 이번 계집앤 어린 것이 여간 잔망스럽지가 않아. 글쎄, 죽기 전에 이런 말을 했다지 않아? 자기자 죽거든 자기 입던 옷을 꼭 그애로 입혀서 묻어 달라고..'
a = 1
for i in 소나기:
    print(i, end='')
    if a % 10 == 0:
        print()
    a = a+1

#3
total = 0
n1 = int(input('시작할 수를 입력해주세요. : '))
n2 = int(input('끝나는 수를 입력해주세요. : '))
for i in range(n1,n2+1,1):
    total = total + i
print('답은 {}입니다.'.format(total))

#4
n = int(input('수를 입력하세요. '))
total = 0.0
for i in range(1,n+1):
    total = total + (float(i+1)/float(i))
print(total)

"""
#5
소설 = input('소설을 입력하세요. ')
total = 1
for i in 소설:
    if i == ' ':
        total = total + 1
if total < 100:
    print('이 소설의 단어 수는 {}개입니다.'.format(total))
else:
    print('이 소설의 단어 수는 100개가 넘어갑니다. 줄이세요.')