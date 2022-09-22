task = input("Введите задачу = ")


if task.find("#"):
    result1 = eval(task.replace("#", "%"))
    print(str(task) + " => " + str(result1))
else:
    pass

# как следующее сделать не понимаю(((((
# if task.find("!"):
#     first, second = task.split("!")
#     suma1 = 0
#     suma2 = 0
#     first2 = int(first)
#     second2 = int(second)
#     while first2 > 0:
#         digit1 = first2 % 10
#         suma1 = int(suma1) + int(digit1)
#         first2 = first2 // 10
#
#     while second2:
#         digit2 = second2 % 10
#         suma2 = suma2 + digit2
#         first2 = first2 // 10
#
#     if suma1 == suma2:
#         print(str(first) + "!" + str(second) + " => " + str(first))
#     elif suma1 > suma2:
#         print(str(first) + "!" + str(second) + " => " + str(first))
#     else:
#         print(str(first) + "!" + str(second) + " => " + str(second))

if task.find("@"):
    first, second = task.split("@")
    if second == first:
        print(str(first) + "@" + str(second) + " => " + str(first))
    elif second > first:
        print(str(first) + "@" + str(second) + " => " + str(second))
    else:
        print(str(first) + "@" + str(second) + " => " + str(first))
else:
    pass


if task.find("$"):
    first, second = task.split("$")
    if len(first) == len(second):
        print(str(first) + "$" + str(second) + " => " + str(first))
    elif len(second) > len(first):
        print(str(first) + "$" + str(second) + " => " + str(second))
    else:
        print(str(first) + "$" + str(second) + " => " + str(first))
else:
    print("нет такой команды")