n = int(input())

sum = 0

# 1부터 100까지이므로 range(1, 101)로 설정
for i in range(1, 101):
    sum += i #현재 숫자에 i를 더함, i는 순차적으로 증가

    # 반복하다 합계가 N 이상이 되었을 때 그때의 i 값을 출력하고 break
    if sum >= n:
        print(i)
        break
