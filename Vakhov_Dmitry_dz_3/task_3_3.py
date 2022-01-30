def thesaurus(*args) -> dict:
    # пишите свою реализацию здесь
    dict_out = {}  # результирующий словарь значений
    for i in args:
        # i: tuple
        # b = list(i)
        # c = b[0]
        c = list(i)[0]
        # dict_out[c] = args[i]
        if c not in dict_out.keys():
            dict_out.update({c: [i]})
        else:
            dict_out[c].append(i)
    # print(type(dict_out))
    # print(type(dict_out['И']))
    # dict_out = sorted(dict_out.items())
    return dict_out
    # return sorted(dict_out.items())


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Анатолий"))
print(sorted(thesaurus("Иван", "Мария", "Петр", "Илья", "Анатолий").items()))
