# from task_3_3 import thesaurus

def thesaurus_adv(*args) -> dict:
    # пишите свою реализацию здесь
    dict_out = {}  # результирующий словарь значений
    my_list: list
    for i in args:
        my_list=i
        c = my_list[my_list.find(' ')+1]
        if c not in dict_out.keys():
            dict_out.update({c: [my_list]})
        else:
            dict_out[c].append(i)
    return dict_out


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева",
                           "Антон Ильин"))


# TODO: Разобраться как сортировать по фамилиям, и как отсортировать по ключу.
