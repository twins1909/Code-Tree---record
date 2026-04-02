string = ["apple", "banana", "grape", "blueberry", "orange"]

n = input()

cnt = 0

for s in string:
    if (s[2] == n) or (s[3] == n):
        print(s)
        cnt += 1

print(cnt)

