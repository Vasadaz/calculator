"""
Скрипт обработки сковок в математическом выражении
"""
# Функция для возврата списка из вложеной функции
def fun_brackets_in_list(math_list: list) -> list:

    # Функция для обработки скобок -> результат записывается в переданный список new_list
    def HIDE_fun_brackets_in_list(old_list: list, new_list: list):
        # Вызов объектов для буферизации __adjusting_i_list, __new_list
        # _starting и _ending объекты для тестирования
        nonlocal __adjusting_i_list, __new_list, _starting, _ending

        """# Объекты для тестирования функции HIDE_fun_brackets_in_list
        print("---------------------------------------------------------------------------")
        print(_starting)
        print(math_list)
        print(__new_list)
        """
        # Объекты для корректировки итереции по old_list
        __copy_old_list = old_list.copy() # Копирование переданого списка для дальнейшего изменение,
        # что позволит не измениять old_list и пройти полную поэлементную итерацию.
        __loop_i_list = 0 # Увеличивается на 1 при каждой итерации по old_list, добавляется в
        # __adjusting_i_list (Условие №2.2), для корректирования итерации после выходы из вложеного списка

        # Цикл for №1
        for i in range(len(old_list)):

            __loop_i_list += 1
            # Условие №1.1
            if __adjusting_i_list[-1] != 0:
                del __copy_old_list[0]
                """# Объекты для тестирования функции HIDE_fun_brackets_in_list
                print("\n\n**************************************")
                print(_starting)
                print(math_list[i], __copy_old_list)
                print(__new_list)
                print(__adjusting_i_list, end="  >>>>>  ")
                """
                __adjusting_i_list[-1] -= 1
                """# Объекты для тестирования функции HIDE_fun_brackets_in_list
                print(__adjusting_i_list)
                print("**************************************")
                """
                continue
            # Условие №1.2
            elif len(__adjusting_i_list) != 1:
                """# Объекты для тестирования функции HIDE_fun_brackets_in_list
                print("\n\n===================================")
                print(_starting)
                print("DELETE", __adjusting_i_list, end="  >>>>>  ")
                """
                del __adjusting_i_list[-1]
                """# Объекты для тестирования функции HIDE_fun_brackets_in_list
                print(__adjusting_i_list)
                print(math_list[i], __copy_old_list)
                print(__new_list)
                print("======================================")
                """
            # Условие №2.1
            if old_list[i] == "(":
                del __copy_old_list[0]
                """# Объекты для тестирования функции HIDE_fun_brackets_in_list
                print("\n\n_________1_________")
                print(_starting)
                print(__adjusting_i_list)
                print(math_list[i], __copy_old_list)
                print(__new_list, end="  >>>>>  ")
                """
                new_list.append([])
                """# Объект для тестирования функции HIDE_fun_brackets_in_list
                print(__new_list)
                _ending += "END "
                _starting += "START "
                """
                HIDE_fun_brackets_in_list(__copy_old_list, new_list[-1])
            # Условие №2.2
            elif old_list[i] == ")":
                del __copy_old_list[0]
                __adjusting_i_list.append(__loop_i_list)
                """# Объекты для тестирования функции HIDE_fun_brackets_in_list
                print("\n\n_________2_________")
                print(_starting)
                print(__adjusting_i_list)
                print(math_list[i], __copy_old_list)
                print(__new_list)
                print(_ending)
                _ending = _ending[0:-4]
                _starting = _starting[0:-6]
                """
                return
            # Условие №2.3
            else:
                del __copy_old_list[0]
                """# Объекты для тестирования функции HIDE_fun_brackets_in_list
                print("\n\n_________3_________")
                print(_starting)
                print(__adjusting_i_list)
                print(math_list[i], __copy_old_list)
                print(__new_list, end="  >>>>>  ")
                """
                new_list.append(old_list[i])

                # print(__new_list)
            #print(_ending)
        return

    # protected
    # Объекты для тестирования функции HIDE_fun_brackets_in_list. Нужны для отслежвания глубины итераций.
    _starting = "START " # Печать этой переменной при каждом запуску функции HIDE_fun_brackets_in_list и при
    # выполнении любого условиия(№1, №2.2) внутри цикла for №1.
    _ending = "END " # Печать этой переменно при каждой итераци внутри цикла for №1 функции HIDE_fun_brackets_in_list.

    # private
    # Объекты для буферезаци функции HIDE_fun_brackets_in_list.
    __adjusting_i_list = [0] # Список для добавления количества итераций внутри вложеного списка при раскрытии скобок
    __new_list = [] # Список для добавления обработаного списка math_list поэлементно

    # Обработка math_list
    HIDE_fun_brackets_in_list(math_list, __new_list)

    # Возврат обработаного списка math_list
    return __new_list

"""
# Объекты для тестирования функции fun_brackets_in_list
math_example = "-1+30+(-4+(5-6)*(-7))-8**2/(-8.8%3)"
list_math_example = ['-1', '+', '30', '+', '(', '-4', '+', '(', '5', '-', '6', ')', '*', '(', '-7', ')', ')', '-', '8', '**', '2', '/', '(', '-8.8', '%', '3', ')']
new_list_math_example = fun_brackets_in_list(list_math_example)
print("\n\n\n\nRESULT:")
print(math_example)
print(list_math_example)
print(new_list_math_example)
"""
