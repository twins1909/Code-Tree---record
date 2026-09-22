n = int(input())


# i = 0 공백 2 별 1
# i = 1 공백 1 별 2
# i = 2 공백 0 별 3

# i = 0 공백 1 별 2개
# i = 1 공백 2 별 1개

for i in range(n):

    for j in range(n - 1 - i):
        print(" ", end="")

    for j in range(i+1):
        print("*", end=" ")

    print()

for i in range(n-1):

    for j in range(i+1):
        print(" ", end="")

    for j in range(n - 1 - i):
        print("*", end=" ")
    print()