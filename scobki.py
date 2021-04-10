# Функция для обработки скобок
def fun_brackets_in_list(old_list: list, new_list: list):
    global __CORECTOR_LIST_SKOBKI
    copy_old_list = old_list.copy()
    corect_in_list = 0
    for el in old_list:
        corect_in_list += 1
        if __CORECTOR_LIST_SKOBKI[-1] != 0:
            __CORECTOR_LIST_SKOBKI[-1] -= 1
            continue
        elif len(__CORECTOR_LIST_SKOBKI) != 1:
            del __CORECTOR_LIST_SKOBKI[-1]

        if el == "(":
            copy_old_list.pop(0)
            new_list.append([])
            fun_brackets_in_list(copy_old_list, new_list[-1])
        elif el == ")":
            copy_old_list.pop(0)
            __CORECTOR_LIST_SKOBKI.append(corect_in_list)
            return
        else:
            copy_old_list.pop(0)
            new_list.append(el)
    return


__CORECTOR_LIST_SKOBKI = [0]
r = []

# Признак fuck = 1 для остановки цикла
"""
__FUCK = 0

while __FUCK == 0:
    # Ввод примера
    primer = input("Чё там?\n")
    if primer == "":
        __FUCK = 1
        break

    # filter_for_primer = lambda n: [] if n == "(" else n
    # Создание списка из строки primer с фильтром от пробелов
    list_primer = [el for el in primer if el != " "]

    new_primer = []

    fun_brackets_in_list(list_primer, new_primer)
    print(new_primer)
"""
