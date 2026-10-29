n = int(input())

# 시작 알파벳 'A'의 아스키 코드값 (65)
curr = ord('A')

for i in range(n):
    for j in range(n):
        # 현재 아스키 코드를 문자로 변환하여 출력
        print(chr(curr), end="")
        
        # 다음 알파벳으로 이동
        curr += 1
        
        # 'Z'를 넘어가면 다시 'A'로 리셋
        if curr > ord('Z'):
            curr = ord('A')
            
    # 한 줄(N개) 출력이 끝나면 줄바꿈
    print()