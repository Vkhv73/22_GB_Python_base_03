def thesaurus(*args) -> dict:
    # пишите свою реализацию здесь
    dict_out = {}  # результирующий словарь значений
    for i in args:
        i: tuple
        b = list(i)
        c = b[0]
        # dict_out[c] = args[i]
        if c not in dict_out.keys():
            dict_out.update({c: [i]})
        else:
            dict_out[c].append(i)
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
