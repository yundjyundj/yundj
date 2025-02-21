str_jumin='851012-1234123'

p=int(str_jumin[7])
y='20'+str_jumin[:2] if p>=3 else '19'+str_jumin[:2]
m=str_jumin[2:4]
d=str_jumin[4:6]
s='남' if p%2==1 else '여'

print(f'출생년도 : {y}')
print(f'출 생 월 : {m}')
print(f'출 생 일 : {d}')
print(f'성    별 : {s}')

