A, B = map(int, input().split())

# 첫 번째 조건 판단
if A < B:
    res1 = 1
else:
    res1 = 0

# 두 번째 조건 판단
if A == B:
    res2 = 1
else:
    res2 = 0

print(res1, res2)