import random
from random import randint
def z1():
    a = [randint(1, 10) for i in range(randint(2, 12))]
    b = int(input("Угадайте число из списка: "))
    print(*a)
    print(b)
    if b in a:
        print("Поздравляю!!!Вы угадали число")
    else:
        print("Такого числа нет!!!")


def z2():
    a = [randint(1, 10) for i in range(randint(1, 10))]
    l = set(a)
    print(*a)
    for i in l:
        b = a.count(i)
        if b > 1:
            print(i, "встречается", b, "раз(a)")
    if len(a) == len(l):
        print("повторяющихся элементов в списке нет")


def z3():
    a = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")
    b = int(input("сколько  вы хотите выходных: "))
    print("Рабочие", *a[:-b])
    print("Выходные", *a[-b:])


def z4():
    from random import sample
    my_gruppa = ["Петров", "Сидоров", "Мочалина", "Кузьмин", "Порталенко"]
    gruppa2 = ["Андерсон", "Порталенко", "Иванов", "Дружинин", "Радин"]
    sport = tuple(random.sample(my_gruppa, 3) + random.sample(gruppa2, 3))
    print("Моя группа: ", *my_gruppa)
    print("другая группа: ", *gruppa2)
    print(*sport, len(sport))
    if "Иванов" in sport:
        print("Фамилия Иванов входит в список секции столько раз:", sport.count("Иванов"))
    else:
        print("Иванова нет  в секции")
