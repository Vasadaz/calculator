#!/usr/bin/python3
"""
The original comments are written in Russian.

My first experience of developing a Python program.
My goal was to create a complete calculator that can:
      1) Accept a string converting it into mathematical operations
      2) Handle numbers with comma or point
      4) Perform mathematical operations + - / //% ** ^
      5) Processing mathematical examples with brackets.
      6) No third-party libraries were used

Мой первый опыт разработки программы на Python.
Перед мной стояла цель создать полноценный калькулятор, который может:
    1) Принимать строку преобразуя её в математические операции
    2) Обрабатывать числа с запятой или точкой
    4) Выполнять математические операции + - / // % ** ^
    5) Обработка математических примеров со скобками
    6) Не использовались сторонние библиотек
"""


def fun_brackets_in_list(math_list: list) -> list:
    # Function for handling parentheses in a mathematical expression
    # by replacing parentheses with a nested list () -> [].
    # Функция обработки скобок в математическом выражении путём замены скобок на вложенный список () -> [].

    def HIDE_fun_brackets_in_list(old_list: list, new_list: list):
        # Function for handling parentheses -> the result is written to the passed list new_list.
        # Функция для обработки скобок -> результат записывается в переданный список new_list.

        # Calling objects to buffer values __adjusting_i_list
        # Referring to elements outside the scope of the function
        # Вызов объектов для буферизации значений __adjusting_i_list
        # Обращение к элементам вне зоны видимости функции
        nonlocal __adjusting_i_list

        # Objects for correcting iterations by old_list.
        # Объекты для корректировки итереций по old_list.
        # Copying the passed list for further modification, which will allow not to change old_list and
        # pass __copy_old_list to iterate in the nested list (Condition №2.1).
        # Копирование переданого списка для дальнейшего изменение, что позволит не измениять old_list и
        # передать __copy_old_list для итерации во вложеном списке(Условие №2.1).
        __copy_old_list = old_list.copy()
        # Increases by 1 at each iteration over old_list, added to __adjusting_i_list (Condition # 2.2),
        # to correct the iteration after exiting the nested list.
        # Увеличивается на 1 при каждой итерации по old_list, добавляется в __adjusting_i_list (Условие №2.2),
        # для корректирования итерации после выходы из вложеного списка.
        __loop_i_list = 0

        # Loop of iterating items from the old_list.
        # Цикл итераций елементов из списка old_list.
        for el in old_list:
            # Counting the number of iterations.
            # Подъсчёт количества итераций.
            __loop_i_list += 1

            # Condition No. 1.1
            # When leaving the created nested list (Condition No. 2.2) into the __adjusting_i_list list
            # adds __loop_i_list. To detect a nested list, this condition is used, then
            # with each next iteration, those elements from __copy_old_list that have already been added are removed
            # into a nested list. The number of these elements is __adjusting_i_list [-1], therefore
            # after removing __copy_old_list [0], there is a decrease by 1 __adjusting_i_list [-1].
            # Mandatory condition __adjusting_i_list [0] must initially contain 0 and always be equal to it.
            # Условие №1.1
            # При выходе из созданого вложеного списка(Условие №2.2) в список __adjusting_i_list
            # добавляется __loop_i_list. Для обнаружения вложенного списка используется данное условие, далее
            # с каждой следующей итерацией удаляются те элементы из __copy_old_list, которые уже добавленны
            # во вложенный список. Количество этих элементов равно __adjusting_i_list[-1], следовательно
            # после удаления __copy_old_list[0] происходит уменьшение на 1 __adjusting_i_list[-1].
            # Обязательное условие __adjusting_i_list[0] должен изначально содержать в себе 0 и всегда быть ему равным.
            if __adjusting_i_list[-1] != 0:
                # Removing __copy_old_list [0] since this item has already been added to new_list
                # Удаление __copy_old_list[0] так, как этот элемент уже добавлен в new_list
                del __copy_old_list[0]

                # Correction of iteration when a nested list is found
                # Коректировка итерации при онаружении вложеного списка
                __adjusting_i_list[-1] -= 1

                # Ending the current iteration and moving on to the next iteration
                # Завершение текущей итерации и переход к следующей итерации
                continue

            # Condition No. 1.2
            # If __adjusting_i_list [-1] == 0, then there is a check for the length of the __adjusting_i_list, so that
            # correct it. If there is more than one element in the list, therefore there were iterations in nested lists
            # and the __copy_old_list adjustment has already occurred in the previous condition.
            # Условие №1.2
            # Если __adjusting_i_list[-1] == 0, то идёт проверка на длину списка __adjusting_i_list, чтобы
            # его скоректировать. Если в списке больше одного элемента, следовательно были итерации во вложеных списках
            # и коректировка __copy_old_list уже произошла в предыдущем условии.
            elif len(__adjusting_i_list) != 1:
                # Adjust the __adjusting_i_list so that __copy_old_list is valid.
                # Коректировка списка __adjusting_i_list так, как __copy_old_list валидный.
                del __adjusting_i_list[-1]

            # Condition No. 2.1
            # Opening brace detection.
            # Условие №2.1
            # Обнаружение открывающей скокобки.
            if el == "(":
                # Removing the __copy_old_list [0] element, since it is "(" and an empty list will be added instead.
                # Удаление элемента __copy_old_list[0], так как это "(" и вместо него будет добавлен пустой список.
                del __copy_old_list[0]

                # Adding an empty list to new_list, which replaces parentheses with a nested list () -> [].
                # The nested list is at index new_list [-1].
                # Добавление в список new_list пустой список, что является заменой скобок на вложеный список () -> [].
                # Вложеный список находится под индексом new_list[-1].
                new_list.append([])

                # Handle elements inside parentheses. __copy_old_list is a shortened version of old_list,
                # and new_list [-1] is a nested list.
                # Обработка элементов внутри скобок. __copy_old_list является укороченой версией old_list,
                # а new_list[-1] является вложеным списком.
                HIDE_fun_brackets_in_list(__copy_old_list, new_list[-1])

            # Condition No. 2.2
            # Detect closing parenthesis.
            # Условие №2.2
            # Обнаружение закрывающей скобки.
            elif el == ")":
                # Adding __loop_i_list to __adjusting_i_list,
                # which will allow to define a nested list (Condition # 1.1).
                # Добавление __loop_i_list в список __adjusting_i_list,
                # что позволит определить вложеный список (Условие №1.1).
                __adjusting_i_list.append(__loop_i_list)

                # Exit HIDE_fun_brackets_in_list, exit the nested list, simulate the closing brackets.
                # Завершение работы HIDE_fun_brackets_in_list, выход из вложеного списка, имитация закрывающей скобки.
                return

            # Condition No. 2.3
            # Adding an item from old_list to new_list. If the previous conditions are skipped,
            # then this item is not parentheses and can be added to new_list.
            # Условие №2.3
            # Добавление элемента из old_list в new_list. Если предыдущие условия пропущены,
            # то этот элемент не является скобками и может быть добавлен в список new_list.
            else:
                # Adding an item from old_list to new_list.
                # Добавление элемента из old_list в new_list.
                new_list.append(el)
                # Removing __copy_old_list [0] since this item has already been added to new_list.
                # Удаление __copy_old_list[0] так, как этот элемент уже добавлен в new_list.
                del __copy_old_list[0]

        # If the iteration over the old_list is over, then the HIDE_fun_brackets_in_list function has been executed.
        # Если итерация по списку old_list закончена, значет функция HIDE_fun_brackets_in_list вывполненна.
        return

    # Objects for buffering the HIDE_fun_brackets_in_list function.
    # Объекты для буферизации функции HIDE_fun_brackets_in_list.
    # List to add the number of iterations inside the nested list when expanding parentheses.
    # Список для добавления количества итераций внутри вложеного списка при раскрытии скобок.
    __adjusting_i_list = [0]
    # List for adding the processed list math_list element by element.
    # Список для добавления обработаного списка math_list поэлементно.
    __new_list = []

    # Processing math_list
    # Обработка math_list
    HIDE_fun_brackets_in_list(math_list, __new_list)

    # Return the processed list math_list
    # Возврат обработаного списка math_list
    return __new_list


def operations(operators: list, args: list):
    # A function to perform all mathematical operations in the correct sequence.
    # Функция для выполнение всех матиматических операций в правильной последовательности.

    def __fix_err_IndexError(index: int):
        # Функция защиты от ошибки IndexError так, как происходит итерация по списку,
        # который можен быть изменён внутри итерации.
        # The function to protect against the IndexError error is how the list is iterated,
        # which can be changed within the iteration.

        # Referring to elements outside the scope of the function.
        # Обращение к элементам вне зоны видимости функции.
        nonlocal operators, args

        # Redirecting an IndexError error.
        # Перенаправление оштбки IndexError.
        try:
            # Checking for the existence of elements in the list.
            # Проверка на существование елементов в списке.
            operators[index] = operators[index]
            args[index + 1] = args[index + 1]

            # On return False, iteration over the list continues.
            # При возврате False итерация по списку продолжается.
            return False
        except IndexError:
            # Returning True stops iterating over the list.
            # При возврате True итерация по списку прекращается.
            return True

    def __right_arg(r_arg, index: int):
        # Function to check the right argument.
        # Функция для проверки правого аргумента.

        # Referring to elements outside the scope of the function.
        # Обращение к элементам вне зоны видимости функции.
        nonlocal operators, args

        # A condition for specifying that the right argument is a list.
        # Условие для определяния того, что правый аргумент является списком.
        if isinstance(r_arg, list):
            # Perform mathematical operations inside the right argument, since it is a list.
            # The result of the operations function is written in place of the right argument (args [index + 1]).
            # Выполнение математических операций внутри правого аргумента, так как он является списком.
            # Результат функции operations записывается вместо правого аргумента (args[index + 1]).
            args[index] = operations(operators[index], args[index])

            # Removing operations associated with the right argument.
            # Удаление операций связанных с правым аргументом.
            del operators[index]

            # Condition to stop the run_math_operation_for function, as this condition says
            # about performing all math operations in the passed lists math_for_operators_list.
            # Условие для остановки функции run_math_operation_for, так как это условие говорит
            # о выполнении всех математических операций в переданных списках math_for_operators_list.
            if len(operators) == 0:
                # Returning True stops the run_math_operation_for function.
                # При возврате True выполнение функции run_math_operation_for останавливается.
                return True
        # If False is returned, execution of the run_math_operation_for function continues.
        # При возврате False выполнение функции run_math_operation_for продолжается.
        return False

    def math_operation(a: float, operator: str, b: float):
        # Function for performing mathematical operations written in operator.
        # Фунцкция для выполнения математической операций записаной в operator.
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

    def __del_DEL():
        # A function to clear the "DEL" elements from the operators and args lists.
        # Функция для очистки списков operators и args от элементов "DEL".

        # Referring to elements outside the scope of the function.
        # Обращение к элементам вне зоны видимости функции.
        nonlocal operators, args

        # Removing "DEL" all elements from the list operators.
        # Удаление "DEL" всех элементов из списка operators.
        operators = [el for el in operators if el != "DEL"]

        # Remove "DEL" all items from the args list.
        # Удаление "DEL" всех элементов из списка args.
        args = [el for el in args if el != "DEL"]

        return

    def run_math_operation_for(math_for_operators_list: list):
        # Function for performing mathematical operations from the list math_for_operators_list.
        # Функция для выполнения математических операции из списка math_for_operators_list.

        # Referring to elements outside the scope of the function.
        # Обращение к элементам вне зоны видимости функции.
        nonlocal operators, args

        # Iterating over an index in a list operators
        # Итерация по индексу в списке operators
        for i in range(len(operators)):
            # Protection against IndexError.
            # Защита от ошибки IndexError.
            if __fix_err_IndexError(i):
                break

            # Condition for defining a mathematical operation.
            # Условие для определения математической операции.
            if operators[i] in math_for_operators_list:
                # Check if the right argument is not a list.
                # Прверка на то, что правый аргумент не является спискомо.
                if __right_arg(args[i + 1], i + 1):
                    return

                # Condition 1.1
                # Condition to define operations for raising to a power of a negative number: (-2) ** 2 = 4
                # Условие 1.1
                # Условие для определения операций по возведению в степень отрицательного числа: (-2)**2 = 4
                if "**" in math_for_operators_list and isinstance(args[i], list):
                    # Expanding parentheses for negative numbers.
                    # Раскрытие скобок для отрицательного числа.
                    args[i] = args[i][0]

                    # Rewriting the processing result into the args list [the next
                    # operation will be performed with this index]
                    # Перезапись резальтата обработки в список args[с этим индексом будет валняться следующая операция]
                    args[i + 1] = math_operation(float(args[i]), operators[i], float(args[i + 1]))

                # Condition 1.2
                # Condition for determining operations for raising to a power of a number before which a minus: -2 ** 2 = -4
                # Условие 1.2
                # Условие для определения операций по возведению в степень числа, перед которым минус: -2**2 = -4
                elif "**" in math_for_operators_list and i == 0 and float(args[i]) < 0:
                    # Rewriting the processing result into the args list [the next operation will be performed with this index]
                    # The result will be written NEGATIVE
                    # Перезапись резальтата обработки в список args[с этим индексом будет валняться следующая операция]
                    # Результат будет записан ОТРИЦАТЕЛЬНЫЙ
                    args[i + 1] = -(math_operation(float(args[i]), operators[i], float(args[i + 1])))

                # Condition 1.3
                # Condition for all other operations.
                # Условие 1.3
                # Условие для всех остальных операций.
                else:
                    # Rewriting the processing result into the
                    # args list [the next operation will be performed with this index]
                    # Перезапись резальтата обработки в список args[с этим индексом будет валняться следующая операция]
                    args[i + 1] = math_operation(float(args[i]), operators[i], float(args[i + 1]))
                # Replacing an already operated number without an index shift
                # Замена уже прооперируемого числа без смещения по индексу
                args[i], operators[i] = "DEL", "DEL"
        # Clearing the operators and args lists of "DEL" elements
        # Очистка списков operators и args от элементов "DEL"
        __del_DEL()
        return

    # Condition for expanding parentheses (nested list) of a negative number, since for it operators = []
    # Условие для раскрытие скобок(вложеного списка) отрицательного числа, так как для него operators = []
    if len(operators) == 0:
        return args[0]

    # Iterate over operators to perform operations within parentheses (nested list)
    # Итерация по operators для выполнения операций внутри скобок(вложеного списка)
    for i_1 in range(len(operators)):
        # Protection against IndexError.
        # Защита от ошибки IndexError.
        if __fix_err_IndexError(i_1):
            break

        # Condition for defining brackets (nested list).
        # Условие для определения скобок(вложеного списка).
        if isinstance(operators[i_1], list):
            # Condition 2.1
            # Condition for expanding parentheses (nested list) of a negative number, since for it operators = []
            # Условие 2.1
            # Условие для раскрытие скобок(вложеного списка) отрицательного числа, так как для него operators = []
            if len(operators[i_1]) == 0:
                # Condition 2.1.1
                # Condition to define operations for raising to a power of a negative number: (-2) ** 2 = 4
                # Условие 2.1.1
                # Условие для определения операций по возведению в степень отрицательного числа: (-2)**2 = 4
                if operators[i_1 + 1] == "**":
                    # Writing the "**" operation to the current index, since operators [i_1 + 1] = []
                    # Запись операции "**" в текущий индекс, так как operators[i_1+1] = []
                    operators[i_1] = operators[i_1 + 1]

                    # Removing a nested list in operators.
                    # Удаление вложеного списка в operators.
                    del operators[i_1 + 1]
                    # The negative number remains in the nested list, this is the marker for Condition 1.1
                    # Отрицательное число остаётся во вложеном списке, это маркер для Условия 1.1

                # Condition 2.1.2
                # Expanding parentheses (nested list) of a negative number.
                # Условие 2.1.2
                # Раскрытие скобок(вложеного списка) отрицательного числа.
                else:
                    # Write the next math operation, since operators [i_1] = []
                    # Запись следующей математической операции, так как operators[i_1] = []
                    operators[i_1] = operators[i_1 + 1]

                    # Deleting the next math operation, since it was written in operators [i_1]
                    # Удаление следующей математической операции, так как она зуписана в operators[i_1]
                    del operators[i_1 + 1]

                    # Replacing a nested list with a negative number
                    # Замена вложеного списка на отрицательно число
                    args[i_1] = (args[i_1][0])

            # Condition 2.2
            # Condition for performing mathematical operations inside brackets (nested list).
            # Условие 2.2
            # Условие для выполнения математических операций внутри скобок(вложеного списка).
            else:
                # Performing mathematical operations inside brackets (nested list).
                # Выполнения математических операций внутри скобок(вложеного списка).
                args[i_1] = operations(operators[i_1], args[i_1])

                # Removing a math operation, since after the operations function in
                # previous line operators [i_1] = []
                # Удаление математической операции, так как после функции operations в
                # предыдущей строке operators[i_1] = []
                del operators[i_1]
    # Sequential execution of mathematical operations
    # Последовательное выполнение математических операций
    run_math_operation_for(["**", "^"])
    run_math_operation_for(["*", "/", "//", "%"])
    run_math_operation_for(["+", "-"])

    # Termination of the operations function with the return of the result after mathematical operations
    # Завершение функции operations с возвратом результата после матеиатических операций
    return args[-1]


def fun_calculator(str_math_example: str):
    # Function of complete processing of a mathematical example using other functions
    # Функция полной обработки математического примера с помощью других функций

    # Operations to convert str_math_example to a list with correct values:
    # 1) Convert str_math_example to a list without spaces x = [el_1 for el_1 in str_math_example if el_1! = ""]
    # 2) Joining the list x into a string x = "". Join (x)
    # 3) Handle situations when the minus is in front of the brackets by replacing - (with -1 * (x = x.replace ("- (", "-1 * (")
    # 4) Create a list with correct values x_list = [el_2 for el_2 in x]

    # Операции по преобразованию str_math_example в список с правильными значениями:
    # 1) Преобразование str_math_example в список без пробелов x=[el_1 for el_1 in str_math_example if el_1 != " "]
    # 2) Склеивание списка х в строку x="".join(x)
    # 3) Обработка ситуаций когда минус перед скобками путём замены -( на -1*( x=x.replace("-(", "-1*(")
    # 4) Создание списка с правильными значениями x_list=[el_2 for el_2 in x]
    math_example_list = [el_2 for el_2 in "".join([el_1 for el_1 in str_math_example if el_1 != " "]).replace("-(", "-1*(")]

    # List for numbers from math_example_list
    # Список для чисел из math_example_list
    args_brackets_list = []

    # List for math operators from math_example_list
    # Список для математических опереторов из math_example_list
    operators_brackets_list = []

    # Index corrector for writing to a list item args_brackets_list, used in Condition 1.2 as an index
    # Коректор индекса для записи в элемент списка args_brackets_list, используется в Условии 1.2 как индекс
    __fix_i_args_brackets_list = 0

    # Loop to form two lists:
    # with arguments -> args_brackets_list
    # with math operators -> operator_brackets_list
    # The parentheses are written to both lists.
    # Цикл для формирования двух списков:
    # с аргументами -> args_brackets_list
    # с математическими операторами -> operators_brackets_list
    # Скобки записываются в оба списка.
    for i in range(len(math_example_list)):
        # Replace comma with full stop.
        # Замена запятой на точку.
        math_example_list[i] = "." if math_example_list[i] == "," else math_example_list[i]

        # Condition 1.1
        # Handle negative numbers.
        # Условие 1.1
        # Обработка отрицательных чисел.
        if (i == 0 and math_example_list[i] == "-") or math_example_list[i - 1:i + 1] == ['(', '-']:
            # Create a new item in args_brackets_list and write to it.
            # Создание нового элемента в args_brackets_list с запись в него минуса.
            args_brackets_list.append(math_example_list[i])

        # Condition 1.2
        # Definitions of integers and decimal numbers.
        # Условие 1.2
        # Определения целых и десятичных чисел.
        elif math_example_list[i].isdigit() or math_example_list[i] == ".":
            # Redirecting an IndexError because the element at the given index may not exist.
            # Перенаправление ошибки IndexError, т.к. элемент с данным индексом может не существовать.
            try:
                # Adding an item to an existing item in the args_brackets_list.
                # Добавление элемента к существующему элементу в списке args_brackets_list.
                args_brackets_list[__fix_i_args_brackets_list] += math_example_list[i]
            except IndexError:
                # Create an item in the args_brackets_list.
                # Создание элемента в списке args_brackets_list.
                args_brackets_list.append(math_example_list[i])

        # Condition 1.3
        # Defining brackets.
        # Условие 1.3
        # Определение скобок.
        elif math_example_list[i] == "(" or math_example_list[i] == ")":
            # Add brackets to args_brackets_list and operators_brackets_list
            # Добавление скобок в args_brackets_list и operators_brackets_list
            args_brackets_list.append(math_example_list[i])
            operators_brackets_list.append(math_example_list[i])

            # Adjust the index for writing to the list item args_brackets_list, used in Condition 1.2 as the index.
            # Коректировка индекса для записи в элемент списка args_brackets_list, используется в Условии 1.2 как индекс.
            __fix_i_args_brackets_list += 1

        # Condition 1.4
        # Definition of math operator **
        # Условие 1.4
        # Определение математического оператора **
        elif math_example_list[i + 1] == "*":
            # Writing a mathematical operator to the list operators_brackets_list **
            # Запись в сисок operators_brackets_list математического оператора **
            operators_brackets_list.append("**")

            # Adjust the index for writing to the list item args_brackets_list, used in Condition 1.2 as the index.
            # Коректировка индекса для записи в элемент списка args_brackets_list, используется в Условии 1.2 как индекс.
            __fix_i_args_brackets_list += 1

            # Duplicate protection * in the next iteration.
            # Защита от дублирования * в следующей итерации.
            math_example_list[i + 1] = "DEL"

        # Condition 1.5
        # Definition of math operator //
        # Условие 1.5
        # Определение математического оператора //
        elif math_example_list[i + 1] == "/":
            # Writing a mathematical operator to the list operators_brackets_list //
            # Запись в сисок operators_brackets_list математического оператора //
            operators_brackets_list.append("//")

            # Adjust the index for writing to the list item args_brackets_list, used in Condition 1.2 as the index
            # Коректировка индекса для записи в элемент списка args_brackets_list, используется в Условии 1.2 как индекс
            __fix_i_args_brackets_list += 1

            # Duplicate protection / in the next iteration.
            # Защита от дублирования / в следующей итерации.
            math_example_list[i + 1] = "DEL"

        # Condition 1.6
        # Define math operators + - * / ^
        # Условие 1.6
        # Определение математических операторов + - * / ^
        elif math_example_list[i] != "DEL":
            # Writing math operators to the list operators_brackets_list + - * / ^
            # Запись в сисок operators_brackets_list математических операторов + - * / ^
            operators_brackets_list.append(math_example_list[i])

            # Adjust the index for writing to the list item args_brackets_list, used in Condition 1.2 as the index
            # Коректировка индекса для записи в элемент списка args_brackets_list, используется в Условии 1.2 как индекс
            __fix_i_args_brackets_list += 1
    # Expanding brackets. () -> []
    # Раскрытие скобок. () -> []
    list_args = fun_brackets_in_list(args_brackets_list)
    list_operators = fun_brackets_in_list(operators_brackets_list)

    # Perform arithmetic operations.
    # Выполнение арифмитических  операций.
    answer = operations(list_operators, list_args)

    # Output a response with a condition for converting integers to int.
    # Вывод ответа с условие для преобразования целых цисел в int.
    print("Answer: {}\n".format(int(answer) if answer % 1 == 0 else answer))
    return answer


#"""
# Preview
# Превью
print('''
The original written in Russian.
The calculator performs the following mathematical operations:
     + Addition
     - Subtraction
     * Multiplication
     / Division
    // Integer division
     % Remainder of the division
  ^ ** Exponentiation
    () Operations within brackets
Decimal numbers can be entered separated by periods or commas: 1,1 = 1.1

Калькулятор выполняет следующие математические операции:
    + Сложение
    - Вычитание
    * Умножение
    / Деление
   // Целочисленное деление
    % Остаток от деления
 ^ ** Возведение в степень
   () Операции внутри скобок
Десятичные числа можно вводить через точку или запятую: 1,1 = 1.1
''')

# Loop for entering math examples
# Цикл ввода математических примеров
while True:
    # Entering a math example
    # Ввод математического примера
    math_example = input("Mathematical example:\n")
    
    # Condition for the end of the while loop
    # Условие для завершения цикла while
    if math_example == "":
        break
    
    # Processing math example
    # Обработки матиматического примера
    fun_calculator(math_example)

print("END")
#"""
