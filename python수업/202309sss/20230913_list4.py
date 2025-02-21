#[문제]
candidate=['kim','park','choi'] #후보자
vote=['kim','kim','choi','kim','choi','choi','kim',
      'park','choi','choi','park','choi']

#우리반 반장 선거 후보자가 candidate 리스트에 있습니다.
#우리반 학생들의 투표내역이 vote 리스트에 있습니다.
#각 후보별 득표수를 구해 보세요.  결과 : [3, 2, 6]

result=[]
for can in candidate:
    result.append(vote.count(can))
print(result)
