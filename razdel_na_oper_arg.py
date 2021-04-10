import scobki
# Пример после скобок
list_primer = ['3', '+', '4', '+', ['2', '+', ['2', '-', '1'], '*', '4'], '-', '1']
new_primer = []
scobki.fun_brackets_in_list(list_primer, new_primer)

# Список для формирования чисел из примера
list_digit = []

# Список для формирования опереторов из примера
list_operator = []

# Коректор индекса для звписи в элемент списка list_digit
i_for_filter = 0


# Скелеивание единых чисел в элемент списока list_digit и
# добавление арифмитического оператора в список list_operator
for i in range(len(list_primer)):
    # Замена запятой на точку
    list_primer[i] = "." if list_primer[i] == "," else list_primer[i]

    # Фильтр для определения целых и точечных чисел
    if list_primer[i].isdigit() or list_primer[i] == ".":
        # Перенаправление ошибки, т.к. элемент с данным индексом может не существовать
        try:
            # Добавление к существуещему элементу в списке list_digit
            list_digit[i_for_filter] += list_primer[i]
        except IndexError:
            # Создание элемента в списке list_digit
            list_digit.append(list_primer[i])

    # Запись в сисок list_operator арифмитического оператора **
    elif list_primer[i + 1] == "*":
        list_operator.append("**")
        # Смещение индекса для следующего числа в списке list_digit
        i_for_filter += 1
        # Защита от дублирования * в следующей итерации
        list_primer[i + 1] = "DEL"

        # Запись в сисок list_operator арифмитического оператора //
    elif list_primer[i + 1] == "/":
        list_operator.append("//")
        # Смещение индекса для следующего числа в списке list_digit
        i_for_filter += 1
        # Защита от дублирования / в следующей итерации
        list_primer[i + 1] = "DEL"

    # Запись в сисок list_operator арифмитических операторов + - * / ^
    elif list_primer[i] != "DEL":
        list_operator.append(list_primer[i])
        # Смещение индекса для следующего числа в списке list_digit
        i_for_filter += 1
    # print(i_for_filter, list_digit, list_operator)
