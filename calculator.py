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
fuck = 0

while fuck == 0:
    # Ввод примера
    primer = input("Чё там?\n")
    if primer == "n":
        fuck = 1
        break
    # Создание списка из строки primer с фильтром от пробелов
    list_primer = [el for el in primer if el != " "]

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

    # Выполнение возведение в степень: ** ^
    for i in range(len(list_operator)):
        # print(list_digit, list_operator)
        # Обработка операторов ** ^
        if list_operator[i] == "**" or list_operator[i] == "^":
            # Присвоение класса для обработки операции
            n = ArifmeticOperation()
            # Перезапись резальтата обработки в список list_digit[с этим индексом будет валняться следующая операция]
            list_digit[i + 1] = n.operation(float(list_digit[i]), list_operator[i], float(list_digit[i + 1]))
            # Удаление уже прооперируемого числа из списка list_digit без смещения по индексу
            list_digit[i] = "DEL"
            # Удаление уже прооперируемого перанта из списка list_operator без смещения по индексу
            list_operator[i] = "DEL"

    # Формированиее списка чисел возведённых в степень из списка list_digit отфильтрованный от "DEL"
    pow_list_digit = [el for el in list_digit if el != "DEL"]

    # Формированиее списка арифмитических операций из списка list_operator отфильтрованный от "DEL"
    pow_list_operator = [el for el in list_operator if el != "DEL"]

    # Выполнение приоритетных арифмитических операций: * / // %
    for i in range(len(pow_list_operator)):
        # print(pow_list_digit, pow_list_operator)
        # Обработка приоритетных операторов: * / // % ** ^
        if pow_list_operator[i] == "*" or pow_list_operator[i] == "/" \
                or pow_list_operator[i] == "//" or pow_list_operator[i] == "%":
            # Присвоение класса для обработки операции
            n = ArifmeticOperation()
            # Перезапись резальтата обработки в список
            # pow_list_operator[с этим индексом будет валняться следующая операция]
            pow_list_digit[i + 1] = n.operation(float(pow_list_digit[i]), pow_list_operator[i],
                                                float(pow_list_digit[i + 1]))
            # Удаление уже прооперируемого числа из списка list_digit без смещения по индексу
            pow_list_digit[i] = "DEL"
            # Удаление уже прооперируемого перанта из списка list_operator без смещения по индексу
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
