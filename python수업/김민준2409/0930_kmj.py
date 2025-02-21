a=[85,76,93,69,87]
l=[]
s=[]

# 리스트 a에서 80이상의 요소들은 리스트 l에,
# 그렇지 않은 요소들은 리스트 s에 추가하시오.

for i in a:
    if i>=80:
        l.append(i)
    else:
        s.append(i)

print(f"80이상 : {l}")
print(f"80미만 : {s}")

#==================================
a=[85,76,93,69,87]
e=[]
o=[]

# 리스트 a에서 짝수의 요소들은 리스트 e에,
# 홀수의 요소들은 리스트 o에 추가하시오.

for i in a:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)

print(f"짝수 : {e}")
print(f"홀수 : {o}")
