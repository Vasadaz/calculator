
# Функция для возврата списка из вложеной функции
def fun_brackets_in_list(math_list: list) -> list:

    # Функция для обработки скобок
    def HIDE_fun_brackets_in_list(old_list: list, new_list: list):
        nonlocal __adjusting_i_list, __new_list, _starting, _ending
        """# Объекты для тестирования функции HIDE_fun_brackets_in_list
        print("---------------------------------------------------------------------------")
        print(_starting)
        print(math_list)
        print(__new_list)
        """
        __copy_old_list = old_list.copy()
        __loop_i_list = 0
        # Цикл for №1
        for i in range(len(old_list)):

            __loop_i_list += 1

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
                """
                _ending += "END "
                _starting += "START "
                HIDE_fun_brackets_in_list(__copy_old_list, new_list[-1])
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
                """
                _ending = _ending[0:-4]
                _starting = _starting[0:-6]
                return
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
            print(_ending)
        return

    # protected
    # Объекты для тестирования функции HIDE_fun_brackets_in_list
    _starting = "START " # Печать при каждом запуску функции HIDE_fun_brackets_in_list и при выполнении любого условиия (№1, №2)  внутри цикла for
    _ending = "END " # П

    # private
    # Объекты для функции HIDE_fun_brackets_in_list
    __adjusting_i_list = [0]
    __new_list = []

    HIDE_fun_brackets_in_list(math_list, __new_list)

    return __new_list


# Создание списка из строки primer с фильтром от пробелов
# list_primer = ['(', '-2', ')', '(', '-8', ')']

# list_primer = ['-3', '4', '(', '-2', '(', '5', '7', ')', '(', '-4', '-4',
#               '(', '50', '70', ')', '(', '-40', '-40', ')', ')', ')', '1']
# new_list = fun_brackets_in_list(list_primer)

# print("\n\n\n\n\nВСЁ", new_list)
