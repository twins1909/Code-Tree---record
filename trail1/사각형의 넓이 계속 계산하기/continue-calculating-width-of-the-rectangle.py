while True:

    w_str, h_str, char = input().split()

    w = int(w_str)
    h = int(h_str)

    print(w * h)

    if char == "C":
        break