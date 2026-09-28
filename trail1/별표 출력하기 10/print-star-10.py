n = int(input())

#위 반복: 1 -> 3 -> 2 / 1 -> 4 -> 2 -> 3 / 1 -> 5 -> 2 -> 4 -> 3

# 아래 반복: 2 -> 3 -> 1 / 3 -> 2 -> 4 -> 1 / 3 -> 4 -> 2 -> 5 -> 1

# 1. 위쪽 구간 (i: 0 -> n-1)
for i in range(n):
    if i % 2 == 0:
        count = i // 2 + 1
    else:
        count = n - (i // 2)

    for j in range(count):
        print("*", end=" ")
    print()

# 2. 아래쪽 구간 (i: n-1 -> 0 거꾸로 되감기)
for i in range(n - 1, -1, -1):
    if i % 2 == 0:
        count = i // 2 + 1
    else:
        count = n - (i // 2)

    for j in range(count):
        print("*", end=" ")
    print()