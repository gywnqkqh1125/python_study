text="얄리얄리얄랑셩 얄라리 얄라"

#위치
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])
print(text[6])
print(text[7])
print(text[8])
print(text[9])
print(text[10])
print(text[11])
print(text[12])
print(text[13])

#~부터~까지
result=text[0:4]
print(result)
result=text[0:14]
print(result)

#뒤집기
result=text[::-1]
print(result)


#변수 길이
print(len(text))

#찾기
where=text.find("셩")
print(where)

#몇 개
count=text.count("얄")
print(count)

#글자 바꾸기
replace=text.replace("얄리", "알리")
print(replace)
