name1 = input('Введите имя:')
pnumber1 = input('Введите четырехзначный номер телефона:')
if len(pnumber1) == 4:
    pass
else:
    pnumber1 = input('Введите четырехзначный номер телефона:')
dict1 = {name1: pnumber1}

name2 = input('Введите имя:')
pnumber2 = input('Введите четырехзначный номер телефона:')
if len(pnumber2) == 4:
    pass
else:
    pnumber2 = input('Введите четырехзначный номер телефона:')
dict2 = {name2: pnumber2}

name3 = input('Введите имя:')
pnumber3 = input('Введите четырехзначный номер телефона:')
if len(pnumber3) == 4:
    pass
else:
    pnumber3 = input('Введите четырехзначный номер телефона:')
dict3 = {name3: pnumber3}

directory = dict1 | dict2 | dict3


# print(directory)
# d_keys = directory.keys()
# d_values = directory.values()
# print(d_keys)
# print(d_values)

# directory = {'Иван': 3655, 'Саша': 6526, 'Маша': 9876}

# # как теперь в функцию запихнуть значения словаря?
def convertation(name, pnumber):
