a=[85,76,93,69,87]

# a의 각 요소들이 짝수인지 홀수인지를 구분하여 출력하기
# i%2==0  : i를 2로 나눈 나머지가 0과 같다.

for i in a:
    if i%2==0 :
        print(f"{i} : 짝수")
    else:
        print(f"{i} : 홀수")

#================================================
# a에서 짝수들의 합계와 홀수들의 합계를 구하여 출력하기
# i%2==0  : i를 2로 나눈 나머지가 0과 같다.

atotal=0  # atotal에 짝수의 합계를 구한다.
btotal=0  # btotal에 홀수의 합계를 구한다.
for i in a:
    if i%2==0 :
        atotal=atotal+i
    else:
        btotal=btotal+i

print(f"짝수합계 : {atotal}")
print(f"홀수합계 : {btotal}")
        
