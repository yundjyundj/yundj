a=[85,76,93,69,87]

# 리스트 a에서 80이상의 요소만 출력하시오.
# <참고 1>
# for i in a:
#     print(i)
#
# <참고 2>
# if i>=80:
#     print(i)

for i in a:
    if i>=80:
        print(i)

# 리스트 a에서 80미만의 요소들의 합계를 출력하시오.
total=0
for i in a:
    if i<80:
        total=total+i

print(f"80미만 합계 : {total}")

