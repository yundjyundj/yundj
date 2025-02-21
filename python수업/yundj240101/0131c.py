num=[85,76,93,69,87,50,80]
# 위에서 짝수만 even이라는 리스트에 넣기
even=[]
for n in num:
    if n%2==0:
        even.append(n)

print(even) # [76,50,80]
