# 1. 두 단어를 입력받습니다.
str1, str2 = input().split()

# 2. str1이 더 길면 str1과 그 길이를 출력
if len(str1) > len(str2):
    print(f"{str1} {len(str1)}")

# 3. str2가 더 길면 str2와 그 길이를 출력 (문제 예시는 Coding 6 이므로 이쪽!)
elif len(str2) > len(str1):
    print(f"{str2} {len(str2)}")
# 4. 길이가 같으면 "same" 출력
else:
    print("same")


# 문자열과 숫자는 더할 수 없으므로 한가지 자료형으로 통일 후에 계산 해야 한다, 메모