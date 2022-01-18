"""
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:

до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""
sec_in_min = 60
sec_in_hour = sec_in_min * 60  # 3600 секунд в часе
sec_in_day = sec_in_hour * 24  # 86400 секунд в сутках


def convert_time(duration: int) -> str:
    # пишите реализацию своей программы здесь
    if duration // sec_in_min == 0:
        s = duration
        return f'{s} сек'
    elif 1 <= duration // sec_in_min < sec_in_min:
        m = duration // sec_in_min
        # s = duration - m*sec_in_min
        s = duration % sec_in_min
        return f'{m} мин {s} сек'
    elif 1 <= duration // sec_in_hour < 24:
        h = duration // sec_in_hour
        m = (duration % sec_in_hour) // sec_in_min
        s = duration - h * sec_in_hour - m * sec_in_min
        return f'{h} час {m} мин {s} сек'
    elif 1 <= duration // sec_in_day:
        d = duration // sec_in_day
        h = (duration % sec_in_day) // sec_in_hour
        m = (duration % sec_in_hour) // sec_in_min
        s = duration - d * sec_in_day - h * sec_in_hour - m * sec_in_min
        return f'{d} дн {h} час {m} мин {s} сек'
    else:
        return 'это слишком мало секунд ))'


duration = 400153
result = convert_time(duration)
print(result)
