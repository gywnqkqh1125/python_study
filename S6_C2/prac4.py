import random as rand

a = []
for i in range(10) :
    b = rand.randint(1,6)
    a.append(b)

print(a)

count = 0
for i in range(10) :
    if a[i] == 1 :
        count = count + 1

print(count)