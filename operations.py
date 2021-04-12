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

starting = ""
ending = ""

def operations(list_operators: list, list_args: list):
    global starting, ending

    def right_arg(r_arg):
        nonlocal  list_operators, list_args, i
        print("_____3_____")
        if isinstance(r_arg, list):

            print(list_args[i+1])
            print(list_operators[i+1])

            list_args[i+1] = operations(list_operators[i+1], list_args[i+1])
            list_operators[i+1] = "DEL"
            if len(list_operators) == 0:
                print("_____TRUE end 3_____")
                return True

            print(list_args)
            print(list_operators)
            print("_____FALSE 2 end 3_____")
            return False
        print("_____FALSE 1 end 3_____")
        return False

    print("------------------------------------------------------------------------")
    starting += "START "
    ending += "END "
    print("BIG",starting)

    # Выполнение возведение в степень: ** ^
    for i in range(len(list_operators)):
        print("\noooooooo START LOOP oooooooo")
        print(starting)
        print(list_args)
        print(list_operators)

        if len(list_operators) == 0:

            print("\n\nANSWER", list_args[0])
            print("BIG", ending, list_args)
            starting = starting[0:-6]
            ending = ending[0:-4]
            print("------------------------------------------------------------------------")

            return list_args[0]

        if isinstance(list_operators[i], list):

            if len(list_operators[i]) == 0:

                print("_____1_____")
                print(list_args[i])
                print(list_operators[i])
                print(list_args[i+1])

                del list_operators[i]
                list_args[i] = list_args[i][0]


                print("_____end 1_____")

            else:

                print("_____2_____")
                print(list_args[i])
                print(list_operators[i])

                list_args[i] = operations(list_operators[i], list_args[i])
                del list_operators[i]

                print("_____end 2_____")
                print(list_args)
                print(list_operators)



        #if right_arg(list_args[i + 1]):
            #return

        # Обработка операторов ** ^
        for i in range(len(list_operators)):
            if list_operators[i] == "**" or list_operators[i] == "^":

                print("\n\nFUCK ** ^")

                if right_arg(list_args[i + 1]):
                    print(ending)
                    starting = starting[0:-6]
                    ending = ending[0:-4]
                    print("------------------------------------------------------------------------")
                    return


                print(list_args)
                print(list_operators)
                print(list_args[i], list_operators[i] , list_args[i+1], end=" = ")

                # Присвоение класса для обработки операции
                n = ArifmeticOperation()
                # Перезапись резальтата обработки в список list_args_brackets[с этим индексом будет валняться следующая операция]
                list_args[i + 1] = n.operation(float(list_args[i]), list_operators[i], float(list_args[i + 1]))
                # Удаление уже прооперируемого числа из списка list_args_brackets без смещения по индексу
                list_args[i] = "DEL"
                # Удаление уже прооперируемого перанта из списка list_for_operators без смещения по индексу
                list_operators[i] = "DEL"

                print(list_args[i+1])

                if len(list_operators) == 1 and list_operators[0] == "DEL":
                    list_args = [el for el in list_args if el != "DEL"]
                    list_operators = [el for el in list_operators if el != "DEL"]
                    print("\n\nANSWER", list_args[0])
                    print("BIG", ending, list_args)
                    starting = starting[0:-6]
                    ending = ending[0:-4]
                    print("------------------------------------------------------------------------")

                    return list_args[0]


        list_operators = [el for el in list_operators if el != "DEL"]
        list_args = [el for el in list_args if el != "DEL"]

        if len(list_operators) == 0:

            print("\n\nANSWER", list_args[0])
            print(ending)
            starting = starting[0:-6]
            ending = ending[0:-4]
            print("------------------------------------------------------------------------")

            return list_args[0]


        # итетных арифмитических операций: * / // %
        for i in range(len(list_operators)):
            if list_operators[i] == "*" or list_operators[i] == "/" \
                    or list_operators[i] == "//" or list_operators[i] == "%":

                print("\n\nFUCK * / // %")

                if right_arg(list_args[i + 1]):
                    print(ending)
                    starting = starting[0:-6]
                    ending = ending[0:-4]
                    print("------------------------------------------------------------------------")
                    return

                print(list_args)
                print(list_operators)
                print(list_args[i], list_operators[i], list_args[i + 1], end=" = ")

                # Присвоение класса для обработки операции
                n = ArifmeticOperation()
                # Перезапись резальтата обработки в список
                # pow_list_operator[с этим индексом будет валняться следующая операция]
                list_args[i + 1] = n.operation(float(list_args[i]), list_operators[i],float(list_args[i + 1]))
                # Удаление уже прооперируемого числа из списка list_args_brackets без смещения по индексу
                list_args[i] = "DEL"
                # Удаление уже прооперируемого перанта из списка list_for_operators без смещения по индексу
                list_operators[i] = "DEL"

                print(list_args[i + 1])
                print(list_args)
                print(list_operators)


                if len(list_operators) == 1 and list_operators[0] == "DEL":
                    list_args = [el for el in list_args if el != "DEL"]
                    list_operators = [el for el in list_operators if el != "DEL"]
                    print("\n\nANSWER", list_args[0])
                    print("BIG", ending, list_args)
                    starting = starting[0:-6]
                    ending = ending[0:-4]
                    print("------------------------------------------------------------------------")

                    return list_args[0]

        list_args = [el for el in list_args if el != "DEL"]
        list_operators = [el for el in list_operators if el != "DEL"]

        if len(list_operators) == 0:

            print("\n\nANSWER", list_args[0])
            print("BIG", ending, list_args)
            starting = starting[0:-6]
            ending = ending[0:-4]
            print("------------------------------------------------------------------------")
            return list_args[0]

        # Выполнение арифмитических операций: + -
        for i in range(len(list_operators)):
            # Обработка операторов: + -
            if list_operators[i] == "+" or list_operators[i] == "-":

                print("\n\nFUCK + -")

                if right_arg(list_args[i + 1]):
                    print(ending)
                    starting = starting[0:-6]
                    ending = ending[0:-4]
                    print("------------------------------------------------------------------------")
                    return

                print(list_args)
                print(list_operators)
                print(list_args[i], list_operators[i], list_args[i + 1], end=" = ")

                # Присвоение класса для обработки операции
                n = ArifmeticOperation()
                # Перезапись резальтата обработки в список
                # new_list_digit[с этим индексом будет валняться следующая операция]
                list_args[i + 1] = n.operation(float(list_args[i]), list_operators[i], float(list_args[i + 1]))
                # Удаление уже прооперируемого числа из списка list_args_brackets без смещения по индексу
                list_args[i] = "DEL"
                # Удаление уже прооперируемого перанта из списка list_for_operators без смещения по индексу
                list_operators[i] = "DEL"

                print(list_args[i + 1])

                if len(list_operators) == 1 and list_operators[0] == "DEL":
                    list_args = [el for el in list_args if el != "DEL"]
                    list_operators = [el for el in list_operators if el != "DEL"]
                    print("\n\nANSWER", list_args[0])
                    print("BIG", ending, list_args)
                    starting = starting[0:-6]
                    ending = ending[0:-4]
                    print("------------------------------------------------------------------------")

                    return list_args[0]

        list_args = [el for el in list_args if el != "DEL"]
        list_operators = [el for el in list_operators if el != "DEL"]

        if len(list_operators) == 0:

            print("\n\nANSWER", list_args[0])
            print("BIG", ending, list_args)
            starting = starting[0:-6]
            ending = ending[0:-4]
            print("------------------------------------------------------------------------")

            return list_args[0]


        print(ending)
        print("oooooooo END LOOP oooooooo")
    print("BIG", ending, list_args)
    starting = starting[0:-6]
    ending = ending[0:-4]
    print("------------------------------------------------------------------------")
    list_args = [el for el in list_args if el != "DEL"]
    list_operators = [el for el in list_operators if el != "DEL"]
    return list_args[-1]
