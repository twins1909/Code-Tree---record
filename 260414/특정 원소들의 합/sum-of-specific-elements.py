matrix = [list(map(int, input().split())) for _ in range(4)]
total = 0

for i in range(4):
    # i가 0이면 j는 0까지, i가 1이면 j는 1까지 돌아야 하므로
    for j in range(i + 1): 
        total += matrix[i][j]

print(total)