cnt_class = 0
cnt_hall = 0
cnt_restroom = 0

n = int(input())

for i in range(1, n+1):
    
    if i % 12 == 0:
        cnt_restroom += 1

    elif i % 3 ==0:
        cnt_hall += 1

    elif i % 2 ==0:
        cnt_class += 1

print(cnt_class, cnt_hall, cnt_restroom)