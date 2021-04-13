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
    print("\nI operations \n", list_args, "\n  ", list_operators, )

    def right_arg(r_arg):

        nonlocal  list_operators, list_args, j

        if isinstance(r_arg, list):
            print("\nI right_arg")
            list_args[j+1] = operations(list_operators[j+1], list_args[j+1])
            del list_operators[j+1]
            if len(list_operators) == 0:
                return True
            return False
        return False

    if len(list_operators) == 0:
        return list_args[0]

    for j in range(len(list_operators)):
        print("\nLOOP \n", list_args, "\n  ", list_operators, )

        try:
            list_operators[j] = list_operators[j]
        except IndexError:
            print("except IndexError")
            return list_args[j]

        if isinstance(list_operators[j], list):
            if len(list_operators[j]) == 0:
                list_operators[j] = list_operators[j+1]
                del list_operators[j+1]
                list_args[j] = list_args[j][0]
                #continue

            else:
                list_args[j] = operations(list_operators[j], list_args[j])
                del list_operators[j]

        # Обработка операторов ** ^
        if list_operators[j] == "**" or list_operators[j] == "^":
            if right_arg(list_args[j + 1]):
                return
            # Присвоение класса для обработки операции
            n = ArifmeticOperation()
            # Перезапись резальтата обработки в список list_args_brackets[с этим индексом будет валняться следующая операция]
            list_args[j + 1] = n.operation(float(list_args[j]), list_operators[j], float(list_args[j + 1]))
            # Удаление уже прооперируемого числа из списка list_args_brackets без смещения по индексу
            list_args[j] = "DEL"
            # Удаление уже прооперируемого перанта из списка list_for_operators без смещения по индексу
            list_operators[j] = "DEL"

        # Выполнение приоритетных арифмитических операций: * / // %
        if list_operators[j] == "*" or list_operators[j] == "/" \
                or list_operators[j] == "//" or list_operators[j] == "%":

            if right_arg(list_args[j + 1]):
                return
            # Присвоение класса для обработки операции
            n = ArifmeticOperation()
            # Перезапись резальтата обработки в список
            # pow_list_operator[с этим индексом будет валняться следующая операция]
            list_args[j + 1] = n.operation(float(list_args[j]), list_operators[j],float(list_args[j + 1]))
            # Удаление уже прооперируемого числа из списка list_args_brackets без смещения по индексу
            list_args[j] = "DEL"
            # Удаление уже прооперируемого перанта из списка list_for_operators без смещения по индексу
            list_operators[j] = "DEL"

        # Выполнение арифмитических операций: + -

        if list_operators[j] == "+" or list_operators[j] == "-":
            if right_arg(list_args[j + 1]):
                return
            # Присвоение класса для обработки операции
            n = ArifmeticOperation()
            # Перезапись резальтата обработки в список
            # new_list_digit[с этим индексом будет валняться следующая операция]
            list_args[j + 1] = n.operation(float(list_args[j]), list_operators[j], float(list_args[j + 1]))
            # Удаление уже прооперируемого числа из списка list_args_brackets без смещения по индексу
            list_args[j] = "DEL"
            # Удаление уже прооперируемого перанта из списка list_for_operators без смещения по индексу
            list_operators[j] = "DEL"

    list_args = [el for el in list_args if el != "DEL"]
    list_operators = [el for el in list_operators if el != "DEL"]

    return list_args[-1]
