"""
Задача "Вызов разом"
"""


def apply_all_func(int_list, *functions):
    dict_ = []
    for i in functions:
        dict_.append([i.__name__, i(int_list)])
    return dict(dict_)


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
