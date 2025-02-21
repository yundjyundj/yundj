#리스트 합계구하기 함수 만들기
def hap(a):
    total=0
    for i in a:
        total+=i
    return total

scores=[85,76,93,69,87]

scores_total=hap(scores)
print(scores_total)


sample=[5,8,9,3,2]
total_sample=hap(sample)
print(total_sample)
