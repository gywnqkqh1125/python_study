"""
#2
x = int(input('x좌표를 입력해 주세요. : '))
y = int(input('y좌표를 입력해 주세요. : '))
사분면 = 0

if x<0 and y>0 :
    사분면 = 1
if x>0 and y>0 :
    사분면 = 2
if x<0 and y<0 :
    사분면 = 3
if x>0 and y<0 :
    사분면 = 4

print('({}, {})는 제 {}사분면에 위치해 있습니다.'.format(x, y, 사분면))

#3
name = input('장수의 이름을 입력해 주세요. ')
무력 = int(input('무력을 입력해 주세요. '))
정치력 = int(input('정치력을 입력해 주세요. '))
지력 = int(input('지력을 입력해 주세요. '))
통솔력 = int(input('통솔력을 입력해 주세요. '))

if 80 <= 무력 or 80 <= 통솔력 :
    print('{}는/은 장군이 될 수 있습니다.'.format(name))
if 70 <= 지력 and 70 <= 정치력 :
    print('{}는/은 군사가 될 수 있습니다.'.format(name))
else :
    print('{}는/은 아무것도 될 수 없습니다.'.format(name))

#4
a = input('lph가 들어가 있는 영어 단어를 말해 보세요. :')

if 'lph' in a :
    print('잘했어요. ^^')
#if not 'lph' in a :
else :
    print('다시 해보세요. 파이팅!')

#5
day = int(input('음력 날짜를 입력해주세요. '))
print('오늘은 음력 {}일 입니다.'.format(day))

if 1 <= day <= 5 :
    print('오늘 달의 모양은 초승달입니다.')
if 6 <= day <= 12 :
    print('오늘 달의 모양은 상현달입니다.')
if 13 <= day <= 19 :
    print('오늘 달의 모양은 보름달입니다.')
if 20 <= day <= 25 :
    print('오늘 달의 모양은 하현달입니다.')
if 26 <= day <= 30 :
    print('오늘 달의 모양은 그믐달입니다.')
"""
#0
gender = input('성별을 입력해주세요.(남/여) ')
h = int(input('키가 몇 cm입니까?'))
e = float(input('시력은 몇입니까?'))

if gender == '남' :
    if h >= 160 and e >= 1.2 :
        print('VR 사격대회에 참가 할 수 있습니다.')
    else :
        print('아쉽네요. 참가할 수 없습니다.')

if gender == '여' :
    if h >= 150 and e >= 1.2 :
        print('VR 사격대회에 참가할 수 있습니다.')
    else :
        print('아쉽네요. 참가할 수 없습니다.')