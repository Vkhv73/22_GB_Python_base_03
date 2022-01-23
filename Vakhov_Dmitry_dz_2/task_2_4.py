# Задание 4

def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов, и формирует список приветствий."""
    # пишите реализацию своей программы здесь
    list_out = list()

    item: str
    for item in list_in:
        name = item.split()[-1].title()
        list_out.append(f'Привет, {name}!')
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)
