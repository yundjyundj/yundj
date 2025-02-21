#ASCII : 정보교환용 미국표준코드  7bit

##print(ord('A'))
##print(ord('a'))
##print(ord('1'))
##
##print(chr(66))

# 어떤 게임에서 park가 'CDADC'를 획득하였다. A는 1점,
# B는 2점, C는 3점, D는 4점, E는 5점이다. park의 점수는?
park='CDADC'
total=0

##for i in park:
##    if i=='A' : total+=1
##    elif i=='B': total+=2
##    elif i=='C': total+=3
##    elif i=='D': total+=4
##    else: total+=5
for i in park:
    total+=ord(i)-ord('A')+1
print(total)











