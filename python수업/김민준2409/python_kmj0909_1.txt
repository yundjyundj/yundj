a=10
b=20
c=a+b
print("a+b=c") # a와 b의 합계를 c에 넣고 이를 출력 하기
print(f"{a} + {b} = {c}")

name="김민준"
age=13
add="전주"
print(f"나는 {add}에사는 {age}세 {name}입니다.")

kor=85
mat=90
eng=93

# ooo의 3과목 총점은 268입니다.
# ooo의 3과목 평균은 268입니다.


print(f"{name}의 3과목 총점은 {kor+mat+eng}입니다.")
print(f"{name}의 3과목 총점은 {(kor+mat+eng)/3}입니다.")
print(f"{name}의 3과목 총점은 {(kor+mat+eng)/3:.1f}입니다.")
