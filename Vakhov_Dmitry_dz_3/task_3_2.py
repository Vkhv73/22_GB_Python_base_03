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
    'One': 'Один',
    'Tne': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
    'Ten': 'Десять',
}


def num_translate(value: str) -> str:
    """Переводит числительное с английского на русский """
    # реализуйте здесь, где хранить необходимые исходные данные определитесь самостоятельно
    # str_out = NUMBER_DICTIONARY.get(value, 'нет такого в словаре')
    if value in NUMBER_DICTIONARY.keys():
        str_out = NUMBER_DICTIONARY.get(value)
        return str_out
    else:
        pass


# def num_translate_v1(value: str) -> str:
#     """Переводит числительное с английского на русский """
#     # реализуйте здесь, где хранить необходимые исходные данные определитесь самостоятельно
#     str_out = NUMBER_DICTIONARY.get(value, 'нет такого в словаре')
#     return str_out


print(num_translate("eleven"))
print(num_translate("one"))
print(num_translate("One"))
print(num_translate("two"))
print(num_translate("eight"))
print(num_translate("zero"))

# print(num_translate_v1("eleven"))
# print(num_translate_v1("one"))
# print(num_translate_v1("two"))
# print(num_translate_v1("eight"))
# print(num_translate_v1("zero"))
