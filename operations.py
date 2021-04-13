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


def operations(list_operators: list, list_args: list):

    def right_arg(r_arg):
        nonlocal  list_operators, list_args, i

        if isinstance(r_arg, list):
            list_args[i+1] = operations(list_operators[i+1], list_args[i+1])
            list_operators[i+1] = "DEL"
            if len(list_operators) == 0:
                return True
            return False
        return False

    # Выполнение возведение в степень: ** ^
    for i in range(len(list_operators)):

        if len(list_operators) == 0:
            return list_args[0]

        if isinstance(list_operators[i], list):
            if len(list_operators[i]) == 0:
                del list_operators[i]
                list_args[i] = list_args[i][0]
            else:
                list_args[i] = operations(list_operators[i], list_args[i])
                del list_operators[i]

        # Обработка операторов ** ^
        for i in range(len(list_operators)):
            if list_operators[i] == "**" or list_operators[i] == "^":
                if right_arg(list_args[i + 1]):
                    return
                # Присвоение класса для обработки операции
                n = ArifmeticOperation()
                # Перезапись резальтата обработки в список list_args_brackets[с этим индексом будет валняться следующая операция]
                list_args[i + 1] = n.operation(float(list_args[i]), list_operators[i], float(list_args[i + 1]))
                # Удаление уже прооперируемого числа из списка list_args_brackets без смещения по индексу
                list_args[i] = "DEL"
                # Удаление уже прооперируемого перанта из списка list_for_operators без смещения по индексу
                list_operators[i] = "DEL"

        list_operators = [el for el in list_operators if el != "DEL"]
        list_args = [el for el in list_args if el != "DEL"]

        # Выполнение приоритетных арифмитических операций: * / // %
        for i in range(len(list_operators)):
            if list_operators[i] == "*" or list_operators[i] == "/" \
                    or list_operators[i] == "//" or list_operators[i] == "%":

                if right_arg(list_args[i + 1]):
                    return
                # Присвоение класса для обработки операции
                n = ArifmeticOperation()
                # Перезапись резальтата обработки в список
                # pow_list_operator[с этим индексом будет валняться следующая операция]
                list_args[i + 1] = n.operation(float(list_args[i]), list_operators[i],float(list_args[i + 1]))
                # Удаление уже прооперируемого числа из списка list_args_brackets без смещения по индексу
                list_args[i] = "DEL"
                # Удаление уже прооперируемого перанта из списка list_for_operators без смещения по индексу
                list_operators[i] = "DEL"

        list_args = [el for el in list_args if el != "DEL"]
        list_operators = [el for el in list_operators if el != "DEL"]

        # Выполнение арифмитических операций: + -
        for i in range(len(list_operators)):
            # Обработка операторов: + -
            if list_operators[i] == "+" or list_operators[i] == "-":
                if right_arg(list_args[i + 1]):
                    return
                # Присвоение класса для обработки операции
                n = ArifmeticOperation()
                # Перезапись резальтата обработки в список
                # new_list_digit[с этим индексом будет валняться следующая операция]
                list_args[i + 1] = n.operation(float(list_args[i]), list_operators[i], float(list_args[i + 1]))
                # Удаление уже прооперируемого числа из списка list_args_brackets без смещения по индексу
                list_args[i] = "DEL"
                # Удаление уже прооперируемого перанта из списка list_for_operators без смещения по индексу
                list_operators[i] = "DEL"

        list_args = [el for el in list_args if el != "DEL"]
        list_operators = [el for el in list_operators if el != "DEL"]

    list_args = [el for el in list_args if el != "DEL"]
    list_operators = [el for el in list_operators if el != "DEL"]
    return list_args[-1]
