age_str_1, gender_1 = input().split()
age_str_2, gender_2 = input().split()

age_1 = int(age_str_1)
age_2 = int(age_str_2)


if (age_1 >= 19 and gender_1 == "M") or (age_2 >= 19 and gender_2 == "M"):
    print("1")

else:
    print("0")