n = int(input())

for i in range(n):
    count = n - i  # 이번 줄에서 별 묶음의 개수이자 묶음당 별 개수
    
    # 묶음을 count번 반복 출력
    for j in range(count):
        # 하나의 묶음 안에 별을 count개 출력
        for k in range(count):
            print("*", end="")
        
        # 묶음과 묶음 사이에 공백 한 칸
        print(" ", end="")
        
    print() 