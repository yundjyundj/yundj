a=[5,8,1,4,2,9]
b=range(5)    # [0,1,2,3,4]
b=range(1,5)  # [1,2,3,4]
b=range(1,5,2)  # [1,3]
b=range(5,0,-1) # [5,4,3,2,1]

for i in a:
    print("안녕") # a요소의 갯수만큼 반복

for i in range(5):
    print("굿모닝")

for i in range(1,6):
    print("*"*i)

for i in range(5,0,-1):
    print("*"*i)

for i in range(1,6):
    print("*"*(6-i))
