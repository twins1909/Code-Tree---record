n = int(input())

curr = ord('A')

for i in range(n):

    print("  " * i, end="")
    
    for j in range(n - i):
        print(chr(curr), end=" ")
        
        curr += 1

        if curr > ord('Z'):
            curr = ord('A')
            
    print()  