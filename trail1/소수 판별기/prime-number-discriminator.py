n = int(input())

# 1은 소수가 아님
if n < 2:
    satisfied = False
else:
    # 일단 소수라고 가정하고 출발
    satisfied = True
    for i in range(2, n):
        # 2부터 n-1 사이에 약수가 하나라도 나오면 소수 탈락
        if n % i == 0:
            satisfied = False
            break

if satisfied:
    print("P")
else:
    print("C")