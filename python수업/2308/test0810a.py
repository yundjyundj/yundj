candidate=['kim','park','choi']
vote=['kim','kim','choi','kim','choi','choi','kim',
      'park','choi','choi','park','choi']

#우리반 반장 선거 후보자가 candidate 리스트에 있습니다.
#우리반 학생들의 투표내역이 vote 리스트에 있습니다.
#각 후보별 득표수를 구해 보세요.
# kim  : 4
# park : 2
# choi : 6

for i in candidate:
    print(f'{i:^4} : {vote.count(i)}')
print('*'*50)
for i in set(vote):
    print(f'{i:^4} : {vote.count(i)}')
