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
    # до минуты
    if duration < sec_in_min:
        s = duration
        return f'{s} сек'
    # до часа
    elif sec_in_min <= duration <= sec_in_hour:
        m = duration // sec_in_min
        s = duration % sec_in_min
        return f'{m} мин {s} сек'
    # до суток
    elif sec_in_hour <= duration < sec_in_day:
        h = duration // sec_in_hour
        m = (duration % sec_in_hour) // sec_in_min
        s = duration % sec_in_min
        return f'{h} час {m} мин {s} сек'
    # больше суток
    elif sec_in_day <= duration:
        d = duration // sec_in_day
        h = (duration % sec_in_day) // sec_in_hour
        m = (duration % sec_in_hour) // sec_in_min
        s = duration % sec_in_min
        return f'{d} дн {h} час {m} мин {s} сек'
    else:
        return 'это слишком мало секунд ))'


duration = 400153
# duration = 8000
result = convert_time(duration)
print(result)
