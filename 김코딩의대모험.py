import random
import time

print('아틀란티스 왕국의 공주, 세델리아 는 사악한 해적 ‘포론’에게 납치되어 미우타우로스 동굴에 갇히게 되었습니다. 공주를 구하기 위해서는 미우타우로스 동굴을 지키고 있는 다섯 괴물을 차례대로 물리쳐야 합니다. 김코딩은 공주를 구하기 위해 미우타우로스 동굴로 갔어요.')
print('한 문제라도 틀리기만 하면 세델리아 공주는 영영 동굴에 갇히게 되고 게임은 끝나게 됩니다. 그럼 세델리아 공주를 구하기 위해 다같이 떠나볼까요?')
input('진행하려면 엔터키를 누르세요.')

time.sleep(1)
print('첫번째 괴물은 날개달린 사자 페세한!')
time.sleep(2)
print('페세한을 이기기 위해서는 주사위를 굴려 페세한보다 더 높은 숫자가 나와야 합니다.')

페세한 = random.randint(1,5)
time.sleep(1.5)
input('주사위를 굴리려면 엔터키를 누르세요.')
dice = random.randint(2,6)
time.sleep(1.5)

print('페세한의 주사위 : {}, 당신의 주사위 : {}'.format(페세한, dice))

if dice > 페세한 :
    print('페세한을 물리쳤습니다.')

    #2
    time.sleep(2)
    print('두 번째 괴물은 철갑 독수리 휴그바!')
    time.sleep(1.5)
    print('휴그바를 이기기 위해서는 휴그바가 내는 수학 문제를 맞혀야 합니다. 문제는 3 + 8 / 2 - 9 * 3 입니다.')
    answer = int(input('답을 입력해주세요.'))
    time.sleep(1.5)
    if answer == (3 + 8 / 2 - 9 * 3) :
        print('휴그바를 물리쳤습니다.')

        #3
        time.sleep(2)
        print('세 번째 괴물은 불 뿜는 용 드래곤!')
        time.sleep(1.5)
        print('드래곤을 이기기 위해서는 1, 2, 3이라는 세 개의 숫자 중 드래곤이 랜덤으로 뽑은 숫자가 무엇인지 맞추어야 합니다.')
        r = random.randint(1,3)
        answer = int(input('답을 입력해주세요.'))
        time.sleep(1.5)
        if answer == r:
            print('드래곤를 물리쳤습니다.')

            #4
            time.sleep(2)
            print('네 번째 괴물은 피리부는 뱀 스말라!')
            time.sleep(1.5)
            print('스말라를 이기기 위해서는 스말라가 가지고 있는 동전의 개수가 짝수인지 홀수인지 맞추어야 합니다. 스말라는 동전을 1개부터 100개 중 랜덤으로 선택합니다.')
            ra = random.randint(1, 100)
            time.sleep(1.5)
            result = 0
            if ra % 2 == 0 :
                result = '짝수'
            else :
                result = '홀수'
            answer = input('답을 입력해주세요.')
            if answer == result :
                print('스말라를 물리쳤습니다.')

                #5
                time.sleep(2)
                print('다섯 번째 괴물은 뿔 달린 원숭이 아마톤!')
                time.sleep(1.5)
                print('아마톤을 이기기 위해서는 아마톤과의 가위바위보 게임에서 승리해야 합니다.')
                answer = input('가위, 바위, 보 중 하나를 선택해 입력해주세요.')
                ran = random.choice(['가위', '바위', '보'])
                time.sleep(1.5)
                if (answer == '가위' and ran == '보') or (answer == '바위' and ran == '가위') or (answer == '보' and ran == '바위') :
                    print('아마톤를 물리쳤습니다.')
                    time.sleep(2)
                    print('공주를 구해내었습니다! 정말 축하하지 않습니다!(구해봤자 거든요)')
else :
    print('게임에서 패배했습니다.')