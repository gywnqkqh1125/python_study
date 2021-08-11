li = []
n = 1
while len(li) < 10000 :
    total = 0
    n = n +1 
    for i in range(1, n+1) :
        if n % i == 0 :
            total = total + 1
    if total == 2 :
        li.append(n)

print(li)