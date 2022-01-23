# print(dir(str))

# Задание 2

def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""

    new_list = list()
    str_out = ''

    # item: str
    # digit: int
    for item in list_in:
        if item.startswith('+'):
            digit = int(item[1:])
            new_list.extend(['"', f'+{int(digit):02d}', '"'])
        elif item.startswith('-'):
            digit = int(item[1:])
            new_list.extend(['"', f'-{int(digit):02d}', '"'])
        elif item.isdigit():
            digit = int(item)
            # print(digit)
            new_list.extend(['"', f'{int(digit):02d}', '"'])
        else:
            new_list.append(item)

    counter = 0
    for item in new_list:
        if '"' == item:
            counter += 1
            # print(counter)
            if counter % 2 != 0:
                str_out += f'{item}'
                continue

        if counter % 2 != 0:
            str_out += f'{item}'
        else:
            str_out += f'{item} '
    print(new_list)
    print(id(new_list))
    return str_out.strip()


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '-100', 'градусов']
print(id(my_list))
result = convert_list_in_str(my_list)
print(result)
print(id(result))
