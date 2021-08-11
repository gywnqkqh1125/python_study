name1 = '김코딩, 이소엔, 박똑똑'
arr = name1.split(', ')
print(arr)

score = [74, 53, 95]

for i in range(len(arr)):
    print('이름 : {} / 점수 : {}'.format(arr[i], score[i]))