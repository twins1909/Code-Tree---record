n = int(input())

for i in range(n):
    for j in range(n):

        # 첫 번째 줄(i == 0)이거나
        # 홀수 열(j % 2 == 1)이면서 i가 j 이하인 경우
        if i == 0 or (j % 2 == 1 and i <= j):
            print("*", end=" ")

        else:
            print("  ", end="")  # 공백 2칸으로 칸 맞추기

    print()