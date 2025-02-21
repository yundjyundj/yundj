a=[85,76,93,69,87,80]

# 리스트 a에서 홀수의 합계구하기(for, fillter함수와 sum함수사용, comprehension사용)
odd_total=sum(filter(lambda x:x%2==1,a))
print(odd_total)

odd_total=sum([i for i in a if i%2==1])
print(odd_total)

odd_cnt=len(list(filter(lambda x:x%2==1,a)))
print(odd_cnt)
