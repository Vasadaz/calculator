# Функция может обращаться к себеже
def skoba(old_list: list, in_list: list, corect_list: list):
    copy_old_list = old_list.copy()
    corect_in_list = 0
    for el in old_list:
        corect_in_list += 1
        if corect_list[-1] != 0:
            corect_list[-1] -= 1
            continue
        elif len(corect_list) != 1:
            del corect_list[-1]

        if el == "(":
            copy_old_list.pop(0)
            in_list.append([])
            skoba(copy_old_list, in_list[-1], corect_list)
        elif el == ")":
            copy_old_list.pop(0)
            corect_list.append(corect_in_list)
            return
        else:
            copy_old_list.pop(0)
            in_list.append(el)

    return

# Признак fuck = 1 для остановки цикла
__FUCK = 0
__CORECTOR_LIST_SKOBKI = [0]

while __FUCK == 0:
    # Ввод примера
    primer = input("Чё там?\n")
    if primer == "n":
        __FUCK = 1
        break

    filter_for_primer = lambda n: [] if n == "(" else n
    # Создание списка из строки primer с фильтром от пробелов
    list_primer = [el for el in primer if el != " "]

    print(list_primer)
    new_m = []

    skoba(list_primer, new_m, __CORECTOR_LIST_SKOBKI)
    print("\n\n\n",new_m)