def replace_nums(string):
    lst = string.split(" ")
    return lst.insert(0, lst.pop(-1))


print(replace_nums("6 7 8 9 5"))
