# 주민번호에서 출생일을 아래처럼 출력한다.
# 출생일 : 2005년 3월 15일

jumin='050315-4123123'

##if jumin[7]=='1' or jumin[7]=='2': # int(jumin[7])<3
##    y='19'+jumin[0:2]
##else:
##    y='20'+jumin[0:2]

# 한 줄로 된 if
# 참일때 if 조건 else 거짓일때
y='19'+jumin[0:2] if int(jumin[7])<3 else '20'+jumin[0:2]
m=jumin[2:4]
d=jumin[4:6]

print(f'출생일 : {y}년 {m}월 {d}일')
