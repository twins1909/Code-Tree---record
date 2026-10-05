n = int(input())

num = 1

for i in range(n):

    if i % 2 == 0:  # 홀수 번째 줄
        for j in range(n):
            print(num + j, end=" ")

        num += n + 1

    else:  # 짝수 번째 줄
        for j in range(n):
            print(num + j * 2, end=" ")

        num += 2 * n - 1

    print()