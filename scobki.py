# Функция для обработки скобок
def fun_brackets_in_list(old_list: list, new_list: list):
    #print("---------------------------------------------------------------------------")
    global __CORECTOR_LIST_SKOBKI
    copy_old_list = old_list.copy()
    corect_in_list = 0
    for i in range(len(old_list)):
        corect_in_list += 1
        if __CORECTOR_LIST_SKOBKI[-1] != 0:
            __CORECTOR_LIST_SKOBKI[-1] -= 1
            continue
        elif len(__CORECTOR_LIST_SKOBKI) == 0:
            del __CORECTOR_LIST_SKOBKI[-1]
        #print(old_list[i - 1:i + 1])

        if old_list[i - 1:i + 1] == [')', '(']:
            #print("\n\n1_________")
            del copy_old_list[0:4]
            new_list.append([])
            fun_brackets_in_list(copy_old_list, new_list[-1])
            continue
        elif old_list[i] == "(":
            #print("\n\n2_________")
            del copy_old_list[0]
            new_list.append([])
            fun_brackets_in_list(copy_old_list, new_list[-1])
        elif old_list[i] == ")":
            #print("\n\n3_________")
            del copy_old_list[0]
            __CORECTOR_LIST_SKOBKI.append(corect_in_list)
            return
        else:
            #print("\n\n4_________")
            del copy_old_list[0]
            new_list.append(old_list[i])

        #print(new_list)
        #print("--------------------")

    return


__CORECTOR_LIST_SKOBKI = [0]

# Признак fuck = 1 для остановки цикла
"""
__FUCK = 0

while __FUCK == 0:
    # Ввод примера
    primer = input("Чё там?\n")
    if primer == "":
        __FUCK = 1
        break"""

# Создание списка из строки primer с фильтром от пробелов
list_primer = ['(', '-2', ')', '(', '-8', ')']
list_primer = ['3', '+', '4', '+', '(', '2', '+', '(', '2', '-', '7', ')', '(', '4', ')', ')',  '-', '1']
new_primer = []

fun_brackets_in_list(list_primer, new_primer)
print("\n\n\n\n\nВСЁ", new_primer)
