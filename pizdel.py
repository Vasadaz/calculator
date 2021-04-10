import scobki

list_primer = ['-', '3', '+', '4', '+', '(', '2', '+', '(', '-', '2', '-', '1', ')', '*', '4', ')', '-', '1']

# Список для формирования чисел из примера
list_args_brackets = []

# Список для формирования опереторов из примера
list_operators_brackets = []

# Коректор индекса для звписи в элемент списка list_args_brackets
__i_for_filter = 0


# Скелеивание единых чисел в элемент списока list_args_brackets и
# добавление арифмитического оператора в список list_for_operators
for i in range(len(list_primer)):
    # Замена запятой на точку
    list_primer[i] = "." if list_primer[i] == "," else list_primer[i]
    print(list_primer[i:i + 2])
    # Обработка отрицательных чисел
    if (i == 0 and list_primer[i] == "-") or list_primer[i - 1 :i + 1] == ['(', '-']:
        list_args_brackets.append(list_primer[i])

    # Фильтр для определения целых и точечных чисел
    elif list_primer[i].isdigit() or list_primer[i] == ".":
        # Перенаправление ошибки, т.к. элемент с данным индексом может не существовать
        try:
            # Добавление к существуещему элементу в списке list_args_brackets
            list_args_brackets[__i_for_filter] += list_primer[i]
        except IndexError:
            # Создание элемента в списке list_args_brackets
            list_args_brackets.append(list_primer[i])

    # Помечаем скобки в оба новых списка
    elif list_primer[i] == "(" or list_primer[i] == ")":
        list_args_brackets.append(list_primer[i])
        list_operators_brackets.append(list_primer[i])
        __i_for_filter += 1
    # Запись в сисок list_for_operators арифмитического оператора **
    elif list_primer[i + 1] == "*":
        list_operators_brackets.append("**")
        # Смещение индекса для следующего числа в списке list_args_brackets
        __i_for_filter += 1
        # Защита от дублирования * в следующей итерации
        list_primer[i + 1] = "DEL"

        # Запись в сисок list_for_operators арифмитического оператора //
    elif list_primer[i + 1] == "/":
        list_operators_brackets.append("//")
        # Смещение индекса для следующего числа в списке list_args_brackets
        __i_for_filter += 1
        # Защита от дублирования / в следующей итерации
        list_primer[i + 1] = "DEL"

    # Запись в сисок list_for_operators арифмитических операторов + - * / ^
    elif list_primer[i] != "DEL":
        list_operators_brackets.append(list_primer[i])
        # Смещение индекса для следующего числа в списке list_args_brackets
        __i_for_filter += 1
    print(__i_for_filter, list_args_brackets, list_operators_brackets)

list_args = []
scobki.fun_brackets_in_list(list_args_brackets, list_args)

list_operators = []
scobki.fun_brackets_in_list(list_operators_brackets, list_operators)

print(list_args, list_operators)
