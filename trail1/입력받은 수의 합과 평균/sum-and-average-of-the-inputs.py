n = int(input())

cnt = 0
sum_val = 0
mean_val = 0

for _ in range(n):

    num = int(input())

    cnt += 1
    sum_val += num

mean_val = sum_val / cnt

print(sum_val, f"{mean_val:.1f}")