a, b = map(int, input().split())
0 <= a and b <= 9

arr =[a, b]

for i in range(8):
    rs1 = arr[-1] + arr[-2]
    rs2 = rs1 % 10
    arr.append(rs2)
    
print(*arr)