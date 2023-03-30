def replace_f(string, index):
    _lst = list(string)
    _lst[index] = "_"
    string = "".join(_lst)
    # string[index] = "_"
    return string

def find_f(string, first_index="No", last_index="No"):
    f_index = string.find("f")
    if f_index == -1 and first_index == "No":
        return
    elif f_index != -1 and first_index == "No":
        first_index = f_index
        string = replace_f(string, first_index)
        print(string)
        find_f(string, first_index)
    elif f_index != -1 and first_index != "No":
        last_index = f_index
        string = replace_f(string, last_index)
        print(string)
        find_f(string, first_index, last_index)
    else:
        return f" Hi {first_index}, {last_index}"

print(find_f("office"))