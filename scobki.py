# Функция для обработи скобок.
# Скобки преобразуются в список, а элементы скобок стяновятся элементами этого списка.
# Аргумениы функции:
# 1) old_list - математическое вырыжение в виде списка без пробелов;
# 2) new_list - пустой список для записи обработаного математическое выражения, () --> [].
# Пример:
# 3 + 4 + (2 + (2 - 1) * 4) - 1
# old_list = ['3', '+', '4', '+', '(', '2', '+', '(', '2', '-', '1', ')', '*', '4', ')', '-', '1']
# new_list = ['3', '+', '4', '+', ['2', '+', ['2', '-', '1'], '*', '4'], '-', '1']
def fun_brackets_in_list(old_list: list, new_list: list):
    # Приватный глобальный список для добавления в него количества проеденых итераций внутри скобок.
    # Защита от дублирования уже добавленных элементов в список new_list при
    # завершении вызванной функции внутри самой функции, так как в высшей функции итерация остановилась на
    # элементе равном "(", а низшая функция уже обработала елементы до ")".
    global __ADJUSTMENT_LIST_BRACKETS
    copy_old_list = old_list.copy()
    corect_in_list = 0
    for el in old_list:
        corect_in_list += 1
        if __ADJUSTMENT_LIST_BRACKETS[-1] != 0:
            __ADJUSTMENT_LIST_BRACKETS[-1] -= 1
            continue
        elif len(__ADJUSTMENT_LIST_BRACKETS) != 1:
            del __ADJUSTMENT_LIST_BRACKETS[-1]

        if el == "(":
            copy_old_list.pop(0)
            new_list.append([])
            fun_brackets_in_list(copy_old_list, new_list[-1])
        elif el == ")":
            copy_old_list.pop(0)
            __ADJUSTMENT_LIST_BRACKETS.append(corect_in_list)
            return
        else:
            copy_old_list.pop(0)
            new_list.append(el)
    return


# Признак __STOP_AND_EXIT = 1 для остановки цикла
__STOP_AND_EXIT = 0
__ADJUSTMENT_LIST_BRACKETS = [0]

while __STOP_AND_EXIT == 0:
    # Ввод примера
    primer = input("Чё там?\n")
    if primer == "":
        __STOP_AND_EXIT = 1
        break

    # Создание списка из строки primer с фильтром от пробелов
    list_primer = [el for el in primer if el != " "]

    print(list_primer)

    new_m = []
    fun_brackets_in_list(list_primer, new_m)
    print("\n\n\n", new_m)
