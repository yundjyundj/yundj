num=[85,76,93,69,87,50,80]
cnt=0
e_cnt=0 # 짝수 갯수
o_cnt=0 # 홀수 갯수

for n in num:
    cnt+=1
    if n%2==0:
        e_cnt+=1
    else:
        o_cnt+=1
print(f'짝수 갯수 : {e_cnt}')
print(f'홀수 갯수 : {o_cnt}')
print(f' 총  갯수 : {cnt}')
# 짝수 갯수 : 3
# 홀수 갯수 : 4
#  총  갯수 : 7
