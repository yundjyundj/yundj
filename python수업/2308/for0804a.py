scores=[85,76,93,69,87]

print(f'scores의 요소의 갯수 : {len(scores)}')

##for score in scores:
##    print(score,end=' ')

for score in scores:
    if score>=80:
        print(f'성적 : {score}, 판정 : 합격')
    else:
        print(f'성적 : {score}, 판정 : 불합격')
