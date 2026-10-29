n = int(input())

curr = ord('A')

for i in range(n):

    for j in range(i+1):

        print(chr(curr), end="")

        curr += 1

        if curr > ord('Z'):
            curr = ord('A')

    print()