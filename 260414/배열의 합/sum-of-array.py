# 출력은 가능하지만 변수가 많아지만 하나하나 코딩하기 어려워짐
#arr1 = list(map(int, input().split()))
#arr2 = list(map(int, input().split()))
#arr3= list(map(int, input().split()))
#arr4 = list(map(int, input().split()))

#print(sum(arr1))
#print(sum(arr2))
#print(sum(arr3))
#print(sum(arr4)) 

# 이런 상황에서 2차원 배열을 사용하여 코드가 길어지는 것을 방지한다

# 1. 4줄의 입력을 받아 바로 2차원 배열로 만든다, 리스트 컴프레헨션을 이용
matrix = [list(map(int, input().split())) for _ in range(4)]

# 2. 각 줄(행)을 하나씩 꺼내며 합을 구한다
for i in range(4):
    row_sum = sum(matrix[i])
    print(row_sum)