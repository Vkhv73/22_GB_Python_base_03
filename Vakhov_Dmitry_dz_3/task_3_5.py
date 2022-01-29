import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int, can_repeat=False, **kwargs) -> list:
    """Возвращает список шуток в количестве count"""
    # пишите реализацию своей программы здесь
    max_count = min(len(nouns), len(adverbs), len(adjectives))
    count = int(input(f'Сколько шуток хотите получить? Но не более {max_count} '))
    if count > max_count:
        count = max_count
    list_out = []

    for _ in range(count):
        if can_repeat:
            list_out.append(' '.join(random.choice(kwargs[j]) for j in kwargs.keys()))
        else:
            noun, adverb, adjective = [random.choice(kwargs[j]) for j in kwargs.keys()]
            list_out.append(' '.join([noun, adverb, adjective]))
            kwargs['nouns'].remove(noun)
            kwargs['adverbs'].remove(adverb)
            kwargs['adjectives'].remove(adjective)

    return list_out


# print(get_jokes(2, nouns=nouns, adverbs=adverbs, adjectives=adjectives))
print(get_jokes(10, nouns=nouns, adverbs=adverbs, adjectives=adjectives))
