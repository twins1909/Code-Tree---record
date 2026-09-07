cnt = 0
sum_val = 0
mean_val = 0

for _ in range(10):

    num = int(input())

    if (0 <= num <= 200):
        cnt += 1
        sum_val += num

mean_val = sum_val / cnt

print(sum_val, f"{mean_val:.1f}")