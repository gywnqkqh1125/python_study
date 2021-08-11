def 시력(sight) :
    if sight >= 1.2 :
        return '눈이 상당히 좋으시네요.'
    if sight >= 0.6 :
        return '눈이 나쁘지는 않지만 조심하세요.'
    else :
        return '눈이 상당히 나쁘네요. 잘 관리해야 해요.'

see = float(input('시력을 입력하세요.: '))
print(시력(see))
