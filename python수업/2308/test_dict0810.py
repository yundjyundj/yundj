# 어떤 게임에서 park가 'CDADC'를 획득하였다. A는 1점,
# B는 2점, C는 3점, D는 4점, E는 5점이다. park의 점수는?
park='CDADC'
total=0

score=dict(zip('ABCDE',[1,2,3,4,5]))

for i in park:
    total+=score[i]
print(total)
