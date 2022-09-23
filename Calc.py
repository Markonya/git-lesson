task = input("Введите задачу = ")

if "#" in task:
    result1 = eval(task.replace("#", "%"))
    print(str(task) + " => " + str(result1))

if "!" in task:
    first, second = task.split("!")
    first_str = list(first)
    first_num = map(int, first_str)
    sum1 = sum(first_num)
    print(sum1)

    second_str = list(second)
    second_num = map(int, second_str)
    sum2 = sum(second_num)
    print(sum2)

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
