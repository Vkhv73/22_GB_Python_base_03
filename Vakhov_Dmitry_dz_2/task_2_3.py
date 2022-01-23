# Задание 3

def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""

    str_out = ""
    item: str
    digit: int
    for item in list_in:
        if item.startswith('+'):
            digit = int(item[1:])
            str_out += f'"+{digit:02d}" '
        elif item.startswith('-'):
            digit = int(item[1:])
            str_out += f'"-{digit:02d}" '
        elif item.isdigit():
            digit = int(item)
            str_out += f'"{int(digit):02d}" '
        else:
            str_out += f'{item} '

    return str_out.strip()


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов']
print(id(my_list))
result = convert_list_in_str(my_list)
print(result)
print(id(result))
