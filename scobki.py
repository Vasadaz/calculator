# Функция может обращаться к себеже
def get_depth(l):
    if isinstance(l, list):
        t = ()
        for itm in l:
            t += get_depth(itm)
        return 1 + max(t)
    return 0

# Признак fuck = 1 для остановки цикла
fuck = 0

while fuck == 0:
    # Ввод примера
    primer = input("Чё там?\n")
    if primer == "n":
        fuck = 1
        break
    # Создание списка из строки primer с фильтром от пробелов
    list_primer = [el for el in primer if el != " "]

m = ['3', '4', '2', '2', '1', '4', '1', ['+', '+', '(', '+', '(', '-', ')', [['*'], ')', '-']]]

print(get_depth(m))
