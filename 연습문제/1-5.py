li = list()
n1 = int(input('첫 번째 숫자를 입력해주세요. '))
n2 = int(input('두 번째 숫자를 입력해주세요. '))
temp = 1
while not (temp > n1 or temp > n2) :
    if n1 % temp == 0 and n2 % temp == 0 :
        li.append(temp)
        print('공약수: ', temp)
    temp += 1

print(li)