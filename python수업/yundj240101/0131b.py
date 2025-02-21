num=[85,76,93,69,87]
# 위에서 80이상인 값들만 hap이라는 리스트에 넣기
hap=[]
for n in num:
    if n>=80:
        hap.append(n)

print(hap) # [85,93,87]
