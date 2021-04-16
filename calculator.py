"""
My first Python's program
"""


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


# Функция обработки скобок в математическом выражении путём замены скобок на вложеный список () -> [].
def fun_brackets_in_list(math_list: list) -> list:
    # Функция для обработки скобок -> результат записывается в переданный список new_list.
    def HIDE_fun_brackets_in_list(old_list: list, new_list: list):
        # Вызов объектов для буферизации __adjusting_i_list, __new_list
        # _starting и _ending объекты для тестирования.
        nonlocal __adjusting_i_list, __new_list
        # Объекты для корректировки итереции по old_list.
        __copy_old_list = old_list.copy()  # Копирование переданого списка для дальнейшего изменение,
        # что позволит не измениять old_list и передать __copy_old_list для итерации во вложеном списке(# Условие №2.1).
        __loop_i_list = 0  # Увеличивается на 1 при каждой итерации по old_list, добавляется в
        # __adjusting_i_list (Условие №2.2), для корректирования итерации после выходы из вложеного списка.

        # Цикл for №1.
        for el in old_list:

            __loop_i_list += 1
            # Условие №1.1
            # При выходе из созданого вложеного списка(Условие №2.2) в список __adjusting_i_list
            # добавляется __loop_i_list. Для обнаружения вложенного списка используется данное условие, далее
            # с каждой следующей итерацией удаляются те элементы из __copy_old_list, которые уже добавленны
            # во вложенный список. Количество этих элементов равно __adjusting_i_list[-1], следовательно
            # после удаления __copy_old_list[0] происходит уменьшение на 1 __adjusting_i_list[-1].
            # Обязательное условие __adjusting_i_list[0] должен изначально содержать в себе 0 и всегда быть ему равным.
            if __adjusting_i_list[-1] != 0:
                # Удаление __copy_old_list[0] так, как этот элемент уже добавлен в new_list
                # __copy_old_list[0] == el
                del __copy_old_list[0]
                # Коректировка итерации при онаружении вложеного списка
                __adjusting_i_list[-1] -= 1
                # Завершение текущей итерации и переход к следующей итерации
                continue
            # Условие №1.2
            # Если __adjusting_i_list[-1] == 0, то идёт проверка на длину списка __adjusting_i_list, чтобы
            # его скоректировать. Если в списке больше одного элемента, следовательно были итерации во вложеных списках
            # и коректировка __copy_old_list уже произошла в предыдущем условии.
            elif len(__adjusting_i_list) != 1:
                # Коректировка списка __adjusting_i_list так, как __copy_old_list валидный.
                del __adjusting_i_list[-1]
            # Условие №2.1
            # Обнаружения скокобок.
            if el == "(":
                # Удаление элемента __copy_old_list[0] так, как это "(" и вместо него будет добавлен пустой список.
                # __copy_old_list[0] == el
                del __copy_old_list[0]
                # Добавление в список new_list пустой список, что является заменой скобок на вложеный список () -> [].
                # Вложеный список находится под мндексом new_list[-1].
                new_list.append([])
                # Обработка элементов внутри скобок. __copy_old_list является укороченой версией old_list,
                # а new_list[-1] является вложеным списком.
                HIDE_fun_brackets_in_list(__copy_old_list, new_list[-1])
            # Условие №2.2
            elif el == ")":
                # Добавление __loop_i_list в список __adjusting_i_list,
                # что позволит определить вложеный список (Условие №1.1)
                __adjusting_i_list.append(__loop_i_list)
                # Завершение работы HIDE_fun_brackets_in_list, выход из вложеного списка, имитация закрывающей скобки.
                return
            # Условие №2.3
            # Добавление элемента из old_list в new_list. Если предыдущие условия пропущены,
            # то этот элемент не является кобками и может быть добавлен в список new_list
            else:
                # Добавление элемента из old_list в new_list
                new_list.append(el)
                # Удаление __copy_old_list[0] так, как этот элемент уже добавлен в new_list.
                # __copy_old_list[0] == el
                del __copy_old_list[0]
        # Если итерация по списку old_list закончена, значет функция HIDE_fun_brackets_in_list вывполненна.
        return

    # private
    # Объекты для буферезаци функции HIDE_fun_brackets_in_list.
    __adjusting_i_list = [0]  # Список для добавления количества итераций внутри вложеного списка при раскрытии скобок
    __new_list = []  # Список для добавления обработаного списка math_list поэлементно

    # Обработка math_list
    HIDE_fun_brackets_in_list(math_list, __new_list)

    # Возврат обработаного списка math_list
    return __new_list


def operations(list_operators: list, list_args: list):
    def right_arg(r_arg):
        nonlocal list_operators, list_args, j
        if isinstance(r_arg, list):
            list_args[j + 1] = operations(list_operators[j + 1], list_args[j + 1])
            del list_operators[j + 1]
            if len(list_operators) == 0:
                return True
        return False


    if len(list_operators) == 0:
        return list_args[0]

    for i in range(len(list_operators)):

        try:
            list_operators[i] = list_operators[i]
            list_args[i + 1] = list_args[i + 1]
        except IndexError:
            break

        for j in range(len(list_operators)):

            try:
                list_operators[j] = list_operators[j]
                list_args[j + 1] = list_args[j + 1]
            except IndexError:
                break

            if isinstance(list_operators[j], list):
                if len(list_operators[j]) == 0:

                    try:
                        list_operators[j] = list_operators[j]
                        list_args[j + 1] = list_args[j + 1]
                    except IndexError:
                        break
                    if list_operators[j + 1] == "**":
                        list_operators[j] = list_operators[j + 1]
                        del list_operators[j + 1]
                    else:
                        list_operators[j] = list_operators[j + 1]
                        del list_operators[j + 1]
                        list_args[j] = (list_args[j][0])
                else:
                    list_args[j] = operations(list_operators[j], list_args[j])
                    del list_operators[j]

        # Обработка операторов ** ^
        for j in range(len(list_operators)):

            try:
                list_operators[j] = list_operators[j]
                list_args[j + 1] = list_args[j + 1]
            except IndexError:
                break

            if list_operators[j] == "**" or list_operators[j] == "^":
                if right_arg(list_args[j + 1]):
                    return
                # Присвоение класса для обработки операции
                if isinstance(list_args[j], list):
                    n = ArifmeticOperation()
                    list_args[j] = list_args[j][0]
                    # Перезапись резальтата обработки в список list_args_brackets[с этим индексом будет валняться следующая операция]
                    list_args[j + 1] = n.operation(float(list_args[j]), list_operators[j], float(list_args[j + 1]))
                    # Удаление уже прооперируемого числа из списка list_args_brackets без смещения по индексу
                    list_args[j] = "DEL"
                    # Удаление уже прооперируемого перанта из списка list_for_operators без смещения по индексу
                elif j == 0 and float(list_args[j]) < 0:
                    n = ArifmeticOperation()
                    # Перезапись резальтата обработки в список list_args_brackets[с этим индексом будет валняться следующая операция]
                    list_args[j + 1] = -(n.operation(float(list_args[j]), list_operators[j], float(list_args[j + 1])))
                    # Удаление уже прооперируемого числа из списка list_args_brackets без смещения по индексу
                    list_args[j] = "DEL"
                    # Удаление уже прооперируемого перанта из списка list_for_operators без смещения по индексу
                    list_operators[j] = "DEL"
                else:
                    n = ArifmeticOperation()
                    # Перезапись резальтата обработки в список list_args_brackets[с этим индексом будет валняться следующая операция]
                    list_args[j + 1] = n.operation(float(list_args[j]), list_operators[j], float(list_args[j + 1]))
                    # Удаление уже прооперируемого числа из списка list_args_brackets без смещения по индексу
                    list_args[j] = "DEL"
                    # Удаление уже прооперируемого перанта из списка list_for_operators без смещения по индексу
                    list_operators[j] = "DEL"

        list_args = [el for el in list_args if el != "DEL"]
        list_operators = [el for el in list_operators if el != "DEL"]

        # Выполнение приоритетных арифмитических операций: * / // %
        for j in range(len(list_operators)):

            try:
                list_operators[j] = list_operators[j]
                list_args[j + 1] = list_args[j + 1]
            except IndexError:
                break

            if list_operators[j] == "*" or list_operators[j] == "/" \
                    or list_operators[j] == "//" or list_operators[j] == "%":

                if right_arg(list_args[j + 1]):
                    return

                # Присвоение класса для обработки операции
                n = ArifmeticOperation()
                # Перезапись резальтата обработки в список
                # pow_list_operator[с этим индексом будет валняться следующая операция]
                list_args[j + 1] = n.operation(float(list_args[j]), list_operators[j], float(list_args[j + 1]))
                # Удаление уже прооперируемого числа из списка list_args_brackets без смещения по индексу
                list_args[j] = "DEL"
                # Удаление уже прооперируемого перанта из списка list_for_operators без смещения по индексу
                list_operators[j] = "DEL"

        list_args = [el for el in list_args if el != "DEL"]
        list_operators = [el for el in list_operators if el != "DEL"]

        # Выполнение арифмитических операций: + -
        for j in range(len(list_operators)):

            try:
                list_operators[j] = list_operators[j]
                list_args[j + 1] = list_args[j + 1]
            except IndexError:
                break

            if list_operators[j] == "+" or list_operators[j] == "-":
                if right_arg(list_args[j + 1]):
                    return

                try:
                    list_operators[i] = list_operators[i]
                except IndexError:
                    break
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


while True:
    # Ввод примера
    math_example = input("Mathematical example:\n")
    # Условие для завершения цикла while
    if math_example == "":
        break

    # Операции по преобразованию math_example в список с правильными значениями:
    # 1) Преобразование math_example в список без пробелов x=[el_1 for el_1 in math_example if el_1 != " "]
    # 2) Склеивание списка х в строку x="".join(x)
    # 3) Обработка ситуаций когда минус перед скобками путём замены -( на -1*( x=x.replace("-(", "-1*(")
    # 4) Создание списка с правильными значениями x_list=[el_2 for el_2 in x]
    math_example_list = [el_2 for el_2 in "".join([el_1 for el_1 in math_example if el_1 != " "]).replace("-(", "-1*(")]

    # Список для формирования чисел из примера
    args_brackets_list = []

    # Список для формирования опереторов из примера
    operators_brackets_list = []

    # Коректор индекса для звписи в элемент списка args_brackets_list
    __fix_i_args_brackets_list = 0

    # Скелеивание единых чисел в элемент списока args_brackets_list и
    # добавление арифмитического оператора в список operators_brackets_list
    for i in range(len(math_example_list)):
        # Замена запятой на точку
        math_example_list[i] = "." if math_example_list[i] == "," else math_example_list[i]
        # Обработка отрицательных чисел
        if (i == 0 and math_example_list[i] == "-") or math_example_list[i - 1:i + 1] == ['(', '-']:
            args_brackets_list.append(math_example_list[i])
        # Фильтр для определения целых и точечных чисел
        elif math_example_list[i].isdigit() or math_example_list[i] == ".":
            # Перенаправление ошибки, т.к. элемент с данным индексом может не существовать
            try:
                # Добавление к существуещему элементу в списке args_brackets_list
                args_brackets_list[__fix_i_args_brackets_list] += math_example_list[i]
            except IndexError:
                # Создание элемента в списке args_brackets_list
                args_brackets_list.append(math_example_list[i])

        # Помечаем скобки в оба новых списка
        elif math_example_list[i] == "(" or math_example_list[i] == ")":
            args_brackets_list.append(math_example_list[i])
            operators_brackets_list.append(math_example_list[i])
            __fix_i_args_brackets_list += 1
        # Запись в сисок operators_brackets_list арифмитического оператора **
        elif math_example_list[i + 1] == "*":
            operators_brackets_list.append("**")
            # Смещение индекса для следующего числа в списке args_brackets_list
            __fix_i_args_brackets_list += 1
            # Защита от дублирования * в следующей итерации
            math_example_list[i + 1] = "DEL"

            # Запись в сисок operators_brackets_list арифмитического оператора //
        elif math_example_list[i + 1] == "/":
            operators_brackets_list.append("//")
            # Смещение индекса для следующего числа в списке args_brackets_list
            __fix_i_args_brackets_list += 1
            # Защита от дублирования / в следующей итерации
            math_example_list[i + 1] = "DEL"

        # Запись в сисок operators_brackets_list арифмитических операторов + - * / ^
        elif math_example_list[i] != "DEL":
            operators_brackets_list.append(math_example_list[i])
            # Смещение индекса для следующего числа в списке args_brackets_list
            __fix_i_args_brackets_list += 1

    # Обраюотка скобок
    list_args = fun_brackets_in_list(args_brackets_list)
    list_operators = fun_brackets_in_list(operators_brackets_list)

    # Выполнение арифмитических  операций
    answer = operations(list_operators, list_args)

    # Вывод ответа с условие для преобразования целых цисел в int
    print("Answer: {}\n".format(int(answer) if answer % 1 == 0 else answer))
print("END")
