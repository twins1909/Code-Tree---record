n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i} * {j} = {i * j}", end="") # 일단 식을 출력
        
        # 마지막 칸(n)이 아닐 때만 콤마와 공백을 추가
        if j < n:
            print(", ", end="")
            
    print() # 한 줄 끝나면 줄바꿈