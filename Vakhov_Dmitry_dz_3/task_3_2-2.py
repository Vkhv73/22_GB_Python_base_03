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


# def num_translate_adv(value: str) -> str:
#     """Переводит числительное с английского на русский """
#     if value.istitle():
#         value = value.lower()
#         if value in NUMBER_DICTIONARY.keys():
#             # value.upper()
#             str_out = NUMBER_DICTIONARY.get(value)
#             str_out1 = str_out.capitalize()
#             return str_out1
#
#     else:
#         str_out = NUMBER_DICTIONARY.get(value)
#         return str_out
#     # return str_out

def num_translate_adv(value: str) -> str:
    """Переводит числительное с английского на русский """
    is_title: bool = value.istitle()
    str_out: str = NUMBER_DICTIONARY.get(value.lower())
    return str_out.title() if is_title else str_out


print(num_translate_adv("eleven"))
print(num_translate_adv("one"))
print(num_translate_adv("One"))
print(num_translate_adv("Two"))
print(num_translate_adv("eight"))
print(num_translate_adv("Eight"))
print(num_translate_adv("zero"))
