n = int(input())
nums = list(map(int, input().split()))

for x in nums[::-1]:
    if x % 2 == 0:
        print(x, end=" ")