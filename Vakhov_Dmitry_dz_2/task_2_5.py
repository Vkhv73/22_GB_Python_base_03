# Задание 5

from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    # пишите реализацию своей программы здесь
    list_out = list()
    for item in list_in:
        item = str(item)
        items = item.split('.')
        rub = f'{int(items[0]):02d}'
        kk = '00'
        if len(items) == 2:
            kk = f'{int(items[1]):02d}'
        list_out.append(f'{rub} руб {kk} коп')
    return ', '.join(list_out)


# автоматическая генерация случайных 15 чисел
my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]
print(f'Исходный список: {my_list}')
print('Область памяти исходного списка: ', id(my_list))
result_1 = transfer_list_in_str(my_list)
print(result_1)
print('Область памяти списка result_1: ', id(result_1))


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    # пишите реализацию здесь
    list_in.sort()
    return list_in


# зафиксируйте здесь информацию по исходному списку my_list
result_2 = sort_prices(my_list)
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
print(result_2)
print('Область памяти списка result_2: ', id(result_2))


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    # пишите реализацию здесь
    list_in.sort()
    list_out = list_in[::-1]
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)
print('Область памяти списка result_3: ', id(result_3))


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    # пишите реализацию здесь
    list_in.sort()
    list_out = list_in[-5:]
    print(list_out)
    list_out.sort(reverse=True)
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)
print('Область памяти списка result_4: ', id(result_4))
