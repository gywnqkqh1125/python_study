sight = float(input('시력을 입력하세요. : '))

if sight >= 1.2 :
    print('시력이 상당히 좋으시네요.')
elif sight >= 0.6 :
    print('시력이 나쁘지는 않지만 조심하세요!')
elif sight >= 0.2 :
    print('시력이 조금 안 좋네요. 안경을 써야겠어요!')
else :
    print('눈이 상당히 나빠요. 게임은 절대 금지!')