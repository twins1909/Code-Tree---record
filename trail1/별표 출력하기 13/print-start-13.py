n = int(input())

# 1. 위쪽 패턴 (0부터 n-1까지)
for i in range(n):
    if i % 2 == 0:
        count = n - (i // 2)
    else:
        count = i // 2 + 1

    for j in range(count):
        print("*", end=" ")
    print()

# 2. 아래쪽 패턴 (n-1부터 0까지 거꾸로 되감기)
for i in range(n - 1, -1, -1):
    if i % 2 == 0:
        count = n - (i // 2)
    else:
        count = i // 2 + 1

    for j in range(count):
        print("*", end=" ")
    print()