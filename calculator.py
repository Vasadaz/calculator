import scobki


class ArifmeticOperation:
    # Метод определения арифмитической операции
    def operation(self, a: float, operator: str, b: float):
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            return a / b
        elif operator == "//":
            return a // b
        elif operator == "%":
            return a % b
        elif operator == "**" or operator == "^":
            return a ** b


# Признак fuck = 1 для остановки цикла
__FUCK = 0
#__CORECTOR_LIST_SKOBKI = [0]

while __FUCK == 0:
    # Ввод примера
    primer = input("Чё там?\n")
    if primer == "":
        __FUCK = 1
        break
    # Создание списка из строки primer с фильтром от пробелов
    list_primer = [el for el in primer if el != " "]
    print(list_primer)

    # Список для формирования чисел из примера
    list_args = []

    # Список для формирования чисел из примера cо скобками
    list_args_brackets = []

    # Список для формирования опереторов из примера cо скобками
    list_operators_brackets = []

    # Коректор индекса для звписи в элемент списка list_args_brackets
    __i_for_filter = 0


    # Скелеивание единых чисел в элемент списока list_args_brackets и
    # добавление арифмитического оператора в список list_operators_brackets
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

    # Список для формирования чисел из примера без скобок () --> []
    list_args = []
    scobki.fun_brackets_in_list(list_args_brackets, list_args)

    # Список для формирования опереторов из примера без скобок () --> []
    list_operators = []
    scobki.fun_brackets_in_list(list_operators_brackets, list_operators)

    print(list_args, list_operators)

    # Выполнение возведение в степень: ** ^
    for i in range(len(list_operators)):
        # print(list_args_brackets, list_for_operators)
        # Обработка операторов ** ^
        if list_operators[i] == "**" or list_operators[i] == "^":
            # Присвоение класса для обработки операции
            n = ArifmeticOperation()
            # Перезапись резальтата обработки в список list_args_brackets[с этим индексом будет валняться следующая операция]
            list_args[i + 1] = n.operation(float(list_args[i]), list_operators[i], float(list_args[i + 1]))
            # Удаление уже прооперируемого числа из списка list_args_brackets без смещения по индексу
            list_args[i] = "DEL"
            # Удаление уже прооперируемого перанта из списка list_for_operators без смещения по индексу
            list_operators[i] = "DEL"

    # Формированиее списка чисел возведённых в степень из списка list_args_brackets отфильтрованный от "DEL"
    pow_list_digit = [el for el in list_args if el != "DEL"]

    # Формированиее списка арифмитических операций из списка list_for_operators отфильтрованный от "DEL"
    pow_list_operator = [el for el in list_operators if el != "DEL"]

    # Выполнение приоритетных арифмитических операций: * / // %
    for i in range(len(pow_list_operator)):
        # print(pow_list_digit, pow_list_operator)
        # Обработка приоритетных операторов: * / // %
        if pow_list_operator[i] == "*" or pow_list_operator[i] == "/" \
                or pow_list_operator[i] == "//" or pow_list_operator[i] == "%":
            # Присвоение класса для обработки операции
            n = ArifmeticOperation()
            # Перезапись резальтата обработки в список
            # pow_list_operator[с этим индексом будет валняться следующая операция]
            pow_list_digit[i + 1] = n.operation(float(pow_list_digit[i]), pow_list_operator[i],
                                                float(pow_list_digit[i + 1]))
            # Удаление уже прооперируемого числа из списка list_args_brackets без смещения по индексу
            pow_list_digit[i] = "DEL"
            # Удаление уже прооперируемого перанта из списка list_for_operators без смещения по индексу
            pow_list_operator[i] = "DEL"

    # Формированиее списка чисел из списка pow_list_digit отфильтрованный от "DEL"
    new_list_digit = [el for el in pow_list_digit if el != "DEL"]

    # Формированиее списка арифмитических операций из списка pow_list_operator отфильтрованный от "DEL"
    new_list_operator = [el for el in pow_list_operator if el != "DEL"]

    # print(new_list_operator, new_list_digit)

    # Выполнение арифмитических операций: + -
    for i in range(len(new_list_operator)):
        # Обработка операторов: + -
        if new_list_operator[i] == "+" or new_list_operator[i] == "-":
            # Присвоение класса для обработки операции
            n = ArifmeticOperation()
            # Перезапись резальтата обработки в список
            # new_list_digit[с этим индексом будет валняться следующая операция]
            new_list_digit[i + 1] = n.operation(float(new_list_digit[i]), new_list_operator[i],
                                                float(new_list_digit[i + 1]))
            # Удаление уже прооперируемого числа из списка new_list_digit без смещения по индексу
            new_list_digit[i] = "DEL"
    # print(new_list_digit, new_list_operator)
    print("Ответ 2: {}".format(new_list_digit[-1]))

print("END")
