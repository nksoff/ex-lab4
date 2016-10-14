import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0

    for item in items:
        assert(isinstance(item, dict))
        if len(args) == 1:
            val = item.get(args[0])
            if val is not None:
                yield val
        else:
            res_dict = {key: item.get(key) for key in (set(item.keys()) & set(args)) if item.get(key) is not None}
            if len(res_dict) > 0:
                yield res_dict


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    for i in range(0, num_count):
        yield random.randint(begin, end)
