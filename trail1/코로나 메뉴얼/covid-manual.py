cold1, temp_str_1 = input().split()
temp1 = int(temp_str_1) 

cold2, temp_str_2 = input().split()
temp2 = int(temp_str_2)

cold3, temp_str_3 = input().split()
temp3 = int(temp_str_3)

count_A = 0

if cold1 == "Y" and temp1 >= 37:
    count_A += 1

if cold2 == "Y" and temp2 >= 37:
    count_A += 1

if cold3 == "Y" and temp3 >= 37:
    count_A += 1

if count_A >= 2:
    print("E")
else:
    print("N")