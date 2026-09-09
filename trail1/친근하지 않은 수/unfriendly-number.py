n = int(input())

cnt = 0

for i in range(1, n+1):

    if (i % 2 == 0) or (i % 3 == 0) or (i % 5 == 0):
        continue 
        # 위에 if 조건을 만족하는 수들은 친근한 수들이므로 continue를 통해 그냥 넘어가게 된다

    # if 조건에 만족하는 수, 즉 친근한 수들은 계속 넘어가다가 
    # 조건에 만족하지 않는 수, 즉 친근하지 않은 수가 나오면 cnt의 개수를 1 증가시킨다
    cnt += 1

print(cnt)