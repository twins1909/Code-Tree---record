cnt = 0

while True:
    n = int(input())

    # 짝수인 경우에만 작업 수행
    if n % 2 == 0:
        print(n // 2)
        cnt += 1

        # 짝수 출력 작업을 3번 완료했다면 종료
        if cnt == 3:
            break