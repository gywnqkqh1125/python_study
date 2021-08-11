def 한타(wold) :
    a = input(wold+':')
    if a == wold:
        print('정답입니다.')
    else:
        print('다시 입력하세요.')
        한타(wold)

print('한글 타자 연습입니다. 다음에 제시된 단어를 입력하세요.')
한타('파이썬')
한타('트리케라톱스')