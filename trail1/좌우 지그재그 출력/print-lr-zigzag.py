n = int(input())

num= 0

for i in range(n):

    if i % 2 == 0:

        for j in range(1, n + 1):
            print(i * n + j, end=" ")

    else:
        for j in range((i + 1) * n, i * n, -1):
            print(j, end=" ")

    print()
