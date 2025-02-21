vote=['kim','kim','choi','kim','choi','choi','kim',
      'park','choi','choi','park','choi']

#우리반 반장 선거 후보자가 candidate 리스트에 있습니다.
#우리반 학생들의 투표내역이 vote 리스트에 있습니다.
#각 후보별 득표수를 구해 보세요.
# kim  : 4
# park : 2
# choi : 6

candidate={}
for i in vote:
    if i in candidate:
        candidate[i]+=1
    else:
        candidate[i]=1
print(candidate)
