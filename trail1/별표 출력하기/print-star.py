n = int(input())

# 1. 늘어나는 구간 (1개 ~ N개)
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# 2. 줄어드는 구간 (N-1개 ~ 1개)
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()