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


def operations(list_operators: list, list_args: list, for_operators: list):
    print("\nI ЩЩЩЩЩЩoperations ", for_operators, "\n  ", list_args, "\n  ", list_operators, )

    def clear_del():
        nonlocal list_operators, list_args
        list_operators = [el for el in list_operators if el != "DEL"]
        list_args = [el for el in list_args if el != "DEL"]
        return

    def right_arg(r_arg):
        nonlocal  list_operators, list_args, j
        if isinstance(r_arg, list):
            print("\nI right_arg")
            list_args[j + 1] = operations(list_operators[j + 1], list_args[j +1 ], ["**", "^"])
            list_args[j + 1] = operations(list_operators[j + 1], list_args[j + 1], ["*", "/", "//", "%"])
            list_args[j + 1] = operations(list_operators[j + 1], list_args[j + 1], ["+", "-"])
            del list_operators[j+1]
            if len(list_operators) == 0:
                return True
            return False
        return False

    if len(list_operators) == 0:
        clear_del()
        return list_args[0]

    for j in range(len(list_operators)):
        print("\nLOOP \n", list_args, "\n  ", list_operators, )

        try:
            list_operators[j] = list_operators[j]
        except IndexError:
            print("except IndexError")
            return list_args[-1]


        if isinstance(list_operators[j], list):
            if len(list_operators[j]) == 0:
                list_operators[j] = list_operators[j+1]
                del list_operators[j+1]
                list_args[j] = list_args[j][0]
            else:
                list_args[j] = operations(list_operators[j], list_args[j], ["**", "^"])
                list_args[j] = operations(list_operators[j], list_args[j], ["*", "/", "//", "%"])
                list_args[j] = operations(list_operators[j], list_args[j], ["+", "-"])
                del list_operators[j]


        if list_operators[j] in for_operators:

            if right_arg(list_args[j + 1]):
                clear_del()
                return

            # Присвоение класса для обработки операции
            n = ArifmeticOperation()
            # Перезапись резальтата обработки в список list_args_brackets[с этим индексом будет валняться следующая операция]
            list_args[j + 1] = n.operation(float(list_args[j]), list_operators[j], float(list_args[j + 1]))
            # Удаление уже прооперируемого числа из списка list_args_brackets без смещения по индексу
            list_args[j] = "DEL"
            # Удаление уже прооперируемого перанта из списка list_for_operators без смещения по индексу
            list_operators[j] = "DEL"

            clear_del()

    clear_del()
    print("RETURN", list_args)
    return list_args
