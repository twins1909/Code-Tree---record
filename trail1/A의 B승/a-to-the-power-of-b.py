# a의 b 제곱은 a를 b만큼 곱하는 것
# 따라서 b번 반복할 때 마다 a를 곱하면 된다

a, b = map(int, input().split())

prod = 1

for _ in range(b):

    prod *= a

print(prod)