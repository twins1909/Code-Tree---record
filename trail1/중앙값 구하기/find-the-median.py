a, b, c = map(int, input().split())

# a가 중앙값인 경우
if (a >= b and a <= c) or (a >= c and a <= b):
    print(a)

#  b가 중앙값인 경우
elif (b >= a and b <= c) or (b >= c and b <= a):
    print(b)
    
else:
    print(c)