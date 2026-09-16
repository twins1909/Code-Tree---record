satisfied = True

for _ in range(5):
    num = int(input())

    if num % 3 != 0:
        satisfied = False
        break

if satisfied:
    print("1")

else:
    print("0")