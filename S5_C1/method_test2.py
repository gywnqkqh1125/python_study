def avg(sub1, sub2, sub3) :
    result = (sub1 + sub2 + sub3) / 3
    return result

sco1 = int(input('첫 번째 과목의 점수를 입력해주세요.: '))
sco2 = int(input('두 번째 과목의 점수를 입력해주세요.: '))
sco3 = int(input('세 번째 과목의 점수를 입력해주세요.: '))

score = avg(sco1, sco2, sco3)
print('평균은 %0.1f점 입니다.'%score)