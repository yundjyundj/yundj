r=[1]
s=2
for i in range(1,10):
    m=r[-1]+s
    r.append(m)
    s+=i

print(r)
