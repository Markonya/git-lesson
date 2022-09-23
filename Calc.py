task = input("Введите задачу = ")

if "#" in task:
    result1 = eval(task.replace("#", "%"))
    print(str(task) + " => " + str(result1))

if "!" in task:
    first, second = task.split("!")

    first_num = map(int, first)
    sum1 = sum(first_num)

    second_num = map(int, second)
    sum2 = sum(second_num)

    if sum1 == sum2:
        print(str(first) + "!" + str(second) + " => " + str(first))
    elif sum1 > sum2:
        print(str(first) + "!" + str(second) + " => " + str(first))
    else:
        print(str(first) + "!" + str(second) + " => " + str(second))

elif "@" in task:
    first, second = task.split("@")
    if second == first:
        print(str(first) + "@" + str(second) + " => " + str(first))
    elif second > first:
        print(str(first) + "@" + str(second) + " => " + str(second))
    else:
        print(str(first) + "@" + str(second) + " => " + str(first))


elif "$" in task:
    first, second = task.split("$")
    if len(first) == len(second):
        print(str(first) + "$" + str(second) + " => " + str(first))
    elif len(second) > len(first):
        print(str(first) + "$" + str(second) + " => " + str(second))
    else:
        print(str(first) + "$" + str(second) + " => " + str(first))
else:
    print("нет такой команды")
