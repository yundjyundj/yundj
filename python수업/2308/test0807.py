scores=[8,9,2,6,5,7,3]

#문제1
#scores 리스트에서 1,3,5,7위치 값의 합계와 2,4,6위치의 합계구하기
# 홀수위치 합계 : 18
# 짝수위치 합계 : 22

# 전체 요소중 짝수의 합계 : 16

total=0
for i in range(0,7,2):
    total+=scores[i]
print(f'홀수위치 합계 : {total}')

total=0
for i in range(1,7,2):
    total+=scores[i]
print(f'짝수위치 합계 : {total}')

total=0
for i in scores[::2]:
    total+=i
print(f'홀수위치 합계 : {total}')

total=0
for i in scores[1::2]:
    total+=i
print(f'짝수위치 합계 : {total}')

even_total=0
for i in scores:
    if i%2==0:
        even_total+=i
print(f'짝수 합계 : {even_total}')


even_count=0
for i in scores:
    if i%2==0:
        even_count+=1
print(f'짝수 갯수 : {even_count}')

max_scores=0
for i in scores:
    if max_scores < i:
        max_scores = i
print(f'최대값 : {max_scores}')

max_scores=scores[0]
for i in scores[1:]:
    if max_scores < i:
        max_scores = i
print(f'최대값 : {max_scores}')


min_scores=9
for i in scores:
    if min_scores > i:
        min_scores = i
print(f'최소값 : {min_scores}')

min_scores=scores[0]
for i in scores[1:]:
    if min_scores > i:
        min_scores = i
print(f'최소값 : {min_scores}')


print(sum(scores))
print(max(scores))
print(min(scores))
print(len(scores))


