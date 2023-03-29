def create_menu(days):
    menu = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
    full_menu = menu * ((days // 7) + 1) #Лучше больше, чем меньше
    for porige in full_menu[0:days]:
        print(porige)


create_menu(83)
