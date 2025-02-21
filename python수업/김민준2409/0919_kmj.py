a=[85,76,93,69,87]
b="powerpoint"

a1=len(a) # a리스트의 요소의 갯수
b1=len(b) # b문자열의 글자수

for i in range(a1): # i값이 0,1,2,3,4 로 바뀌면서 print명령이 처리됨
    print(a[i])

print("="*30) # = 를 30번 출력

for i in a: # 여기서 a는 [85,76,93,69,87]이다
    print(i)
