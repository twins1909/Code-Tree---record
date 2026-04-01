n = int(input())

# 개수를 셀 변수를 미리 만들어 둠
count = 0

# 1부터 n 까지 이므로  ragne(1, n+1)로 설정
for i in range(1, n+1):
    if (i % 2 == 0) or (i % 3 == 0) or (i % 5 == 0):
        continue # 친근한 수는 건너뛰기

    count += 1 # 다음 숫자로 이동 후 반복


# 친근하지 않는 숫자를 찾아 몇 개인지 출력
print(count)  