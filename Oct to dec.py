def oct_to_dec(oct):
    lst = []
    flist = []
    value = 0
    for i in str(oct):
        lst.append(i)
    lst.reverse()
    for num in range(len(lst)):
        var_num = (int(lst[num]))*(8**num)
        flist.append(var_num)
    for numz in range(len(flist)):
        value += flist[numz]
    return value

print(oct_to_dec(304))
