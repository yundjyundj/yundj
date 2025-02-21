num=[85,76,93,69,87,50,80]
total=0
e_total=0 # 짝수 합계
o_total=0 # 홀수 합계

for n in num:
    total+=n
    if n%2==0:
        e_total+=n
    else:
        o_total+=n
print(f'짝수 합계 : {e_total}')
print(f'홀수 합계 : {o_total}')
print(f' 총  합계 : {total}')
# 짝수 합계 : 999
# 홀수 합계 : 999
#  총  합계 : 999
