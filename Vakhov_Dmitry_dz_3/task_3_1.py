from typing import Optional

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


def num_translate(value: str) -> Optional[str]:
    """Переводит числительное с английского на русский """
    # реализуйте здесь, где хранить необходимые исходные данные определитесь самостоятельно
    return NUMBER_DICTIONARY.get(value)


# def num_translate_v1(value: str) -> str:
#     """Переводит числительное с английского на русский """
#     # реализуйте здесь, где хранить необходимые исходные данные определитесь самостоятельно
#     str_out = NUMBER_DICTIONARY.get(value, 'нет такого в словаре')
#     return str_out


print(num_translate("eleven"))
print(num_translate("one"))
print(num_translate("two"))
print(num_translate("eight"))
print(num_translate("zero"))

# print(num_translate_v1("eleven"))
# print(num_translate_v1("one"))
# print(num_translate_v1("two"))
# print(num_translate_v1("eight"))
# print(num_translate_v1("zero"))
