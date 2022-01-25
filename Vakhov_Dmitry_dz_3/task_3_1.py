NUMBER_DICTIONARY: dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}


def num_translate(value: str) -> str:
    """Переводит числительное с английского на русский """
    # реализуйте здесь, где хранить необходимые исходные данные определитесь самостоятельно
    # val = dic.get('key1', 'na')
    str_out = NUMBER_DICTIONARY.get(value, 'нет такого в словаре')
    return str_out


print(num_translate("eleven"))
print(num_translate("one"))
print(num_translate("two"))
print(num_translate("eight"))
print(num_translate("zero"))
