n = int(input())

for i in range(1, n+1):

    for j in range(1, n + 1):

        # i=1, j=1 일 때 11이 되도록 (i + j - 2) * 2 계산
        print(11 + 2 * (i + j - 2), end=" ")
        
    print()