##a=[i for i in range(1,10)]
##print(a)

##score=[85,76,93,69,87]
##
##odd_list=[i for i in score if i%2==1]
##print(odd_list)

for i in range(1,4):
    for j in range(1,3):
        print(i,j)

b= [(i,j) for i in range(1,4) for j in range(1,3)]
print(b)

i=1
while i<=5:
    print(f"반복을 {i}번 했어요.")
    i+=1



score=[85,76,93,69,87]
total=0
for i in score:
    total+=i
print(total)



total=0
for i in range(len(score)):
    total+=score[i]
print(total)


total=0
number=1
while number:
    number=int(input('숫자 입력 : '))
    if number==999:break
    total+=number
print(total)



