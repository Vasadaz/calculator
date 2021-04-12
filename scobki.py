"""
Скрипт обработки скобок в математическом выражении путём замены скобок на вложеный список () -> [].
"""


# Функция для возврата списка из вложеной функции.
def fun_brackets_in_list(math_list: list) -> list:
    # Функция для обработки скобок -> результат записывается в переданный список new_list.
    def HIDE_fun_brackets_in_list(old_list: list, new_list: list):
        # Вызов объектов для буферизации __adjusting_i_list, __new_list
        # _starting и _ending объекты для тестирования.
        nonlocal __adjusting_i_list, __new_list, _starting, _ending

        """# Объекты для тестирования функции HIDE_fun_brackets_in_list
        print("---------------------------------------------------------------------------")
        print(_starting)
        print(math_list)
        print(__new_list)
        """
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
                """
                # Объекты для тестирования функции HIDE_fun_brackets_in_list.
                print("\n\n**************************************")
                print(_starting)
                print(math_list[i], __copy_old_list)
                print(__new_list)
                print(__adjusting_i_list, end="  >>>>>  ")
                """
                # Коректировка итерации при онаружении вложеного списка
                __adjusting_i_list[-1] -= 1
                """
                # Объекты для тестирования функции HIDE_fun_brackets_in_list.
                print(__adjusting_i_list)
                print("**************************************")
                """
                # Завершение текущей итерации и переход к следующей итерации
                continue
            # Условие №1.2
            # Если __adjusting_i_list[-1] == 0, то идёт проверка на длину списка __adjusting_i_list, чтобы
            # его скоректировать. Если в списке больше одного элемента, следовательно были итерации во вложеных списках
            # и коректировка __copy_old_list уже произошла в предыдущем условии.
            elif len(__adjusting_i_list) != 1:
                """
                # Объекты для тестирования функции HIDE_fun_brackets_in_list.
                print("\n\n===================================")
                print(_starting)
                print("DELETE", __adjusting_i_list, end="  >>>>>  ")
                """
                # Коректировка списка __adjusting_i_list так, как __copy_old_list валидный.
                del __adjusting_i_list[-1]
                """
                # Объекты для тестирования функции HIDE_fun_brackets_in_list.
                print(__adjusting_i_list)
                print(math_list[i], __copy_old_list)
                print(__new_list)
                print("======================================")
                """
            # Условие №2.1
            # Обнаружения скокобок.
            if el == "(":
                # Удаление элемента __copy_old_list[0] так, как это "(" и вместо него будет добавлен пустой список.
                # __copy_old_list[0] == el
                del __copy_old_list[0]
                """
                # Объекты для тестирования функции HIDE_fun_brackets_in_list
                print("\n\n_________1_________")
                print(_starting)
                print(__adjusting_i_list)
                print(math_list[i], __copy_old_list)
                print(__new_list, end="  >>>>>  ")
                """
                # Добавление в список new_list пустой список, что является заменой скобок на вложеный список () -> [].
                # Вложеный список находится под мндексом new_list[-1].
                new_list.append([])
                """
                # Объект для тестирования функции HIDE_fun_brackets_in_list
                print(__new_list)
                _ending += "END "
                _starting += "START "
                """
                # Обработка элементов внутри скобок. __copy_old_list является укороченой версией old_list,
                # а new_list[-1] является вложеным списком.
                HIDE_fun_brackets_in_list(__copy_old_list, new_list[-1])
            # Условие №2.2
            elif el == ")":
                # Добавление __loop_i_list в список __adjusting_i_list,
                # что позволит определить вложеный список (Условие №1.1)
                __adjusting_i_list.append(__loop_i_list)
                """
                # Объекты для тестирования функции HIDE_fun_brackets_in_list
                print("\n\n_________2_________")
                print(_starting)
                print(__adjusting_i_list)
                print(math_list[i], __copy_old_list)
                print(__new_list)
                print(_ending)
                _ending = _ending[0:-4]
                _starting = _starting[0:-6]
                """
                # Завершение работы HIDE_fun_brackets_in_list, выход из вложеного списка, имитация закрывающей скобки.
                return
            # Условие №2.3
            # Добавление элемента из old_list в new_list. Если предыдущие условия пропущены,
            # то этот элемент не является кобками и может быть добавлен в список new_list
            else:
                """
                # Объекты для тестирования функции HIDE_fun_brackets_in_list
                print("\n\n_________3_________")
                print(_starting)
                print(__adjusting_i_list)
                print(math_list[i], __copy_old_list)
                print(__new_list, end="  >>>>>  ")
                """
                # Добавление элемента из old_list в new_list
                new_list.append(el)
                """
                # Объект для тестирования функции HIDE_fun_brackets_in_list
                print(__new_list)
                """
                # Удаление __copy_old_list[0] так, как этот элемент уже добавлен в new_list.
                # __copy_old_list[0] == el
                del __copy_old_list[0]
            """
            # Объект для тестирования функции HIDE_fun_brackets_in_list
            print(_ending)
            """
        # Если итерация по списку old_list закончена, значет функция HIDE_fun_brackets_in_list вывполненна.
        return

    # protected
    # Объекты для тестирования функции HIDE_fun_brackets_in_list. Нужны для отслежвания глубины итераций.
    _starting = "START "  # Печать этой переменной при каждом запуску функции HIDE_fun_brackets_in_list и при
    # выполнении любого условиия(№1, №2.2) внутри цикла for №1.
    _ending = "END "  # Печать этой переменной при каждой итераци внутри цикла for №1 функции HIDE_fun_brackets_in_list.

    # private
    # Объекты для буферезаци функции HIDE_fun_brackets_in_list.
    __adjusting_i_list = [0]  # Список для добавления количества итераций внутри вложеного списка при раскрытии скобок
    __new_list = []  # Список для добавления обработаного списка math_list поэлементно

    # Обработка math_list
    HIDE_fun_brackets_in_list(math_list, __new_list)

    # Возврат обработаного списка math_list
    return __new_list


"""
# Объекты для тестирования функции fun_brackets_in_list
math_example = "-1+30+(-4+(5-6)*(-7))-8**2/(-8.8%3)"
list_math_example = ['-1', '+', '30', '+', '(', '-4', '+', '(', '5', '-', '6', ')', '*', 
                     '(', '-7', ')', ')', '-', '8', '**', '2', '/', '(', '-8.8', '%', '3', ')']
new_list_math_example = fun_brackets_in_list(list_math_example)
print("\n\n\n\nRESULT:")
print(math_example)
print(list_math_example)
print(new_list_math_example)
"""
