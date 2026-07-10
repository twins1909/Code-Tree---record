a, b = map(int, input().split())

#  일단 정수 몫을 먼저 출력하고 소수점을 찍는다
print(a // b, end=".")

#  첫 번째 나머지를 구한다
remainder = a % b

#  소수점 아래 20번째 자리까지 한 자리씩 구하며 출력한다
for _ in range(20):
    # 나머지에 10을 곱해서 다음 자리로 만든다
    remainder *= 10
    
    # 그걸 b로 나눈 몫이 바로 그 자리에 들어갈 소수점 숫자다
    print(remainder // b, end="")
    
    # 다음 계산을 위해 새로운 나머지를 구한다
    remainder %= b