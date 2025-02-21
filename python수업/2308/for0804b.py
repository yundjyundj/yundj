numbers=[20,33,51,30,70,87,91]
# 20은 홀수입니다.
# 33은 짝수입니다.

for num in numbers:
    if num%2==1:
        print(f'{num}은 홀수입니다.')
    else:
        print(f'{num}은 짝수입니다.')
