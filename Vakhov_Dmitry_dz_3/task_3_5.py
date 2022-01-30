import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    # пишите реализацию своей программы здесь
    max_count = min(len(nouns), len(adverbs), len(adjectives))
    count = int(input(f'Сколько шуток хотите получить? Но не более {max_count} =) '))
    if count > max_count:
        count = max_count
    list_out = []

    for _ in range(count):
        i = random.choice(nouns)
        j = random.choice(adverbs)
        k = random.choice(adjectives)
        list_out.append(' '.join([i, j, k]))
    return list_out


print(get_jokes(10))
