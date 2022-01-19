def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    percent = 'процент'
    if n % 10 == 1 and n % 100 != 11:
        return f'{n} {percent}'
    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 > 20):
        percent = percent + "а"
        return f'{n} {percent}'
    else:
        percent = percent + "ов"
        return f'{n} {percent}'
    # return 'верните отформатированную строку'


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))
