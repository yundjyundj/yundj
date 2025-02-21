s=[85,76,93,69,87] #리스트

print(s)
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print("=======================")
b=len(s)
for i in range(b):
    print(s[i])
print("=======================")
hap=0
for i in range(b):
    hap=hap+s[i]

print(f"s의 합계 : {hap}")
print("=======================")

#s=[85,76,93,69,87]에서 0,2,4번째값들의 합계
hap=0
for i in range(0,b,2):
    hap=hap+s[i]

print(f"s의 짝수번째 합계 : {hap}")
print("=======================")

