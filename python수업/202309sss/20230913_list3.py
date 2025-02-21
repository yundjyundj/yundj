scores=[]
for i in range(5):
    s=int(input('점수 입력 : ')) # scores.append(int(input('점수 입력 : ')))
    scores.append(s)
print(scores)

#scores의 합계 구하기 1

print(sum(scores))

#scores의 합계 구하기 2
total=0
for i in scores:
    total+=i
print(total)
