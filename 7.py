def replace_f(string, index):
    _lst = list(string)
    _lst[index] = "_"
    string = "".join(_lst)
    return string

def find_last_f(string, last_index="NO"):
    if string.find("f") == -1:
        return last_index
    else:
        last_index = string.find("f")
        string = replace_f(string, last_index)
        return find_last_f(string, last_index=last_index)

def find_f(string):
    first_index = string.find("f")
    string = replace_f(string, first_index)
    last_index = find_last_f(string)
    if first_index == -1:
        return
    elif last_index == "NO":
        return first_index
    else:
        return f"{first_index} {last_index}"



print(find_f("I want a high five for this homework."))