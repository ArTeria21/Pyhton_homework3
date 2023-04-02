def replace_f(string, index):
    # Функция "replace_f" заменяет символ строки на другой символ по указанному индексу.

    _lst = list(string)
    _lst[index] = "_"
    # Преобразуем строку в список, заменяем символ на "_".

    string = "".join(_lst)
    # Соединяем элементы списка обратно в строку.

    return string


def find_last_f(string, last_index="NO"):
    # Функция "find_last_f" находит индекс последнего символа "f" в строке.

    if string.find("f") == -1:
        # Если символ "f" в строке не найден, возвращаем последний известный индекс.

        return last_index
    else:
        last_index = string.find("f")
        # Находим индекс последнего символа "f" в строке.

        string = replace_f(string, last_index)
        # Заменяем символ на "_".

        return find_last_f(string, last_index=last_index)
        # Рекурсивно вызываем функцию, передавая ей последний известный индекс.


def find_f(string):
    # Функция "find_f" находит первый и последний символ "f" в строке.

    first_index = string.find("f")
    # Находим индекс первого символа "f" в строке.

    string = replace_f(string, first_index)
    # Заменяем первый символ на "_".

    last_index = find_last_f(string)
    # Находим индекс последнего символа "f" в строке.

    if first_index == -1:
        # Если первый символ "f" в строке не найден, возвращаем "None".

        return
    elif last_index == "NO":
        # Если последний символ "f" в строке не найден, возвращаем первый индекс.

        return first_index
    else:
        # Иначе возвращаем индексы первого и последнего символов "f" через пробел.

        return f"{first_index} {last_index}"




print(find_f("I want a high five for this homework."))
