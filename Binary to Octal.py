def bin_to_oct(b):
    bin = str(b)
    list = []
    digits = []
    for alpha in bin:  # list maker
        list.append(alpha)
    while len(list) % 3 != 0:
            list.insert(0, 0)
# splitter function needs maintance (add if statement for odd numbers)
    for i in range(0, len(list), 3):
        var = list[i:i+3]  # split into 3 sections
        dig_1 = (int(var[0]) * 4) + (int(var[1]) * 2) + \
            (int(var[2]) * 1)  # formula
        digits.append(dig_1)
        s = ''.join(map(str, digits))
    return int(s)
