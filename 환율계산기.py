print('환율계산기')

won = int(input('환전하고 싶은 금액은?'))

usd = 1116.11
print('미국: ', round(won / usd, 2), '＄(달러)')

jpy = 10.62
print('일본: ', round(won / jpy, 2), '￥(엔)')

cny = 172.74
print('중국: ',round(won / cny, 2), '¥(위안)')

thb = 37.14
print('태국: ', round(won / thb, 2), '฿(바트(밧))')

php = 23.24
print('필리핀: ', round(won / php, 2), '₱(페소)')

vnd = 0.048
print('베트남: ', round(won / vnd, 2), '₫(동)')