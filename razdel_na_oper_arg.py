import scobki

# Пример после скобок
list_primer = ['3', '+', '4', '+', ['2', '+', ['2', '-', '1'], '*', '4'], '-', '1']
__new_list = []
scobki.fun_brackets_in_list(list_primer, __new_list)

# Список для формирования чисел из примера
list_args = []

# Список для формирования опереторов из примера
list_operators = []

# Коректор индекса для звписи в элемент списка list_args
__i_for_filter = 0


def razdelitel(list_math_ex: list, list_for_args: list, list_for_operators: list):
    copy_list_math_ex = list_math_ex.copy()
    for i in range(len(list_math_ex)):
        if isinstance(i, list):
            list_for_args.append([])
            list_for_operators.append([])
            razdelitel(copy_list_math_ex[i], list_for_args[-1], list_for_operators[-1])
        else:
            sortirovka(list_math_ex, i, list_for_args, list_for_operators)

    return None


# Скелеивание единых чисел в элемент списока list_args_brackets и
# добавление арифмитического оператора в список list_for_operators

def sortirovka(list_math_ex: list, i_list_math_ex: int, list_for_args: list, list_for_operators: list):
    global __i_for_filter
    # Замена запятой на точку
    list_math_ex[i_list_math_ex] = "." if list_math_ex[i_list_math_ex] == "," else list_math_ex[i_list_math_ex]

    # Фильтр для определения целых и точечных чисел
    if list_math_ex[i_list_math_ex].isdigit() or list_math_ex[i_list_math_ex] == ".":
        # Перенаправление ошибки, т.к. элемент с данным индексом может не существовать
        try:
            # Добавление к существуещему элементу в списке list_args_brackets
            list_for_args[__i_for_filter] += list_math_ex[i_list_math_ex]
        except IndexError:
            # Создание элемента в списке list_args_brackets
            list_for_args.append(list_math_ex[i_list_math_ex])

    # Запись в сисок list_for_operators арифмитического оператора **
    elif list_math_ex[i_list_math_ex + 1] == "*":
        list_for_operators.append("**")
        # Смещение индекса для следующего числа в списке list_args_brackets
        __i_for_filter += 1
        # Защита от дублирования * в следующей итерации
        list_math_ex[i_list_math_ex + 1] = "DEL"

        # Запись в сисок list_for_operators арифмитического оператора //
    elif list_math_ex[i_list_math_ex + 1] == "/":
        list_for_operators.append("//")
        # Смещение индекса для следующего числа в списке list_args_brackets
        __i_for_filter += 1
        # Защита от дублирования / в следующей итерации
        list_math_ex[i_list_math_ex + 1] = "DEL"

    # Запись в сисок list_for_operators арифмитических операторов + - * / ^
    elif list_math_ex[i_list_math_ex] != "DEL":
        list_for_operators.append(list_math_ex[i_list_math_ex])
        # Смещение индекса для следующего числа в списке list_args_brackets
        __i_for_filter += 1
    # print(__i_for_filter, list_args_brackets, list_for_operators)
    __i_for_filter = 0
    return None

razdelitel(__new_list, list_args, list_operators)

print(list_args)
print(list_operators)
