"""
#4-1
a = []
for i in range(-1, -51, -1) :
    a.append(i)
print(a)
#4-2
b = []
for i in range(20, 61) :
    if i % 2 == 1 :
        b.append(i)
print(b)
#4-3
c = []
for i in range(1, 101) :
    if i % 3 == 0 :
        c.append(i)
print(c)
#4-4
d = []
def isSosu(i) :
    n = 2
    count = 0
    while n != i :
        if i % n == 0 :
            count = count + 1
        n = n+1
    if count == 0 :
        d.append(i)
for i in range(2, 101) :
    isSosu(i)
print(d)
print('리스트의 길이: {}'.format(len(d)))
"""
#3
name = ''
li = []

while name != '끝' :
    name = input('우리 반 친구의 이름을 입력해주세요. 다 입력했으면 끝이라고 입력해주세요. ')
    if name != '끝' :
        li.append(name)

print(li)
