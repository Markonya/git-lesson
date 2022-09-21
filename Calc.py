import math

integer1 = int(input("Введите число 1 = "))
integer2 = int(input("Введите число 2 = "))

action = int(input("Введите команду "))

if action == 1:
    result1 = integer2 % integer1
    print(str(integer1) + "#" + str(integer2) + " => " + str(result1))
elif action == 2:
    res1 = 0
    res2 = 0

    while integer1 and integer2:
        res1 += integer1 % 10
        integer1 //= 10
        res2 += integer2 % 10
        integer2 //= 10
    if res1 == res2:
        print("результат одинаков")
    elif res1 > res2:
        print(str(integer1) + "$" + str(integer2) + " => " + str(integer1))
    else:
        print(str(integer1) + "$" + str(integer2) + " => " + str(integer2))

elif action == 3:
        if integer2 == integer1:
            print("Числа равны")
        elif integer2 > integer1:
            print(str(integer1) + "@" + str(integer2) + " => " + str(integer2))
        else:
            print(str(integer1) + "@" + str(integer2) + " => " + str(integer1))
elif action == 4:
     if len(str(integer1)) == len(str(integer1)):
         print(str(integer1) + "$" + str(integer2) + " => " + str(integer1))
     elif len(str(integer1)) > len(str(integer1)):
         print(str(integer1) + "$" + str(integer2) + " => " + str(integer1))
     else:
         print(str(integer1) + "$" + str(integer2) + " => " + str(integer2))
else:
    print("нет такой команды")
