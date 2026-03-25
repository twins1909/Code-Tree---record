y = int(input())

# 1. 가장 까다로운 400의 배수부터 확인!
if y % 400 == 0:
    print("true")
# 2. 그다음으로 까다로운 100의 배수 확인
elif y % 100 == 0:
    print("false")
# 3. 마지막으로 4의 배수 확인
elif y % 4 == 0:
    print("true")
else:
    print("false")