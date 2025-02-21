jumin='050315-4123123'
cur_year=2023
y=int(jumin[0:2])
s=int(jumin[7])

if s%4==1 or s%4==2 : bir_year=1900+y
else:bir_year=2000+y

age=cur_year - bir_year

if s%2==1 : sex='남'
else  : sex='여'


# 나이 : 18,  성별 : 여
print(f'나이 : {age},  성별 : {sex}')
