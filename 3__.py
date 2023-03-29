def replace_nums(string):
    lst = string.split(" ")
    for i in range(0, len(lst)+1):
        if i == len(lst):
            lst[i] = lst[0]
        else:
            lst[i] = lst[i+1]
    return lst



print(replace_nums("6 7 8 9 5"))
