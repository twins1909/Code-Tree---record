n = int(input())

for i in range(n):
    for j in range(2*i + 1): # j의 범위가 홀수가 되도록 설정한다 2 * i + 1을 통해서
        print("*", end="")
    print()