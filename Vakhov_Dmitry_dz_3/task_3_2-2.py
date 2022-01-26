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
    if value.istitle():
        value = value.lower()
        if value in NUMBER_DICTIONARY.keys():
            # value.upper()
            str_out = NUMBER_DICTIONARY.get(value)
            str_out1 = str_out.capitalize()
            return str_out1

    else:
        str_out = NUMBER_DICTIONARY.get(value)
        return str_out
    # return str_out


print(num_translate("eleven"))
print(num_translate("one"))
print(num_translate("One"))
print(num_translate("Two"))
print(num_translate("eight"))
print(num_translate("Eight"))
print(num_translate("zero"))
