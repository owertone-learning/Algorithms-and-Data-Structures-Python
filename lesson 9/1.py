'''
1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib
задача считается не решённой.
'''

from hashlib import sha1


def rk(s: str):
    assert len(s) > 0, 'Строки не могут быть пустыми'

    len_str = len(s)
    subs_list = {}

    for i in range(len_str):
        for j in range(i + 1, len_str + 1):
            subs = s[i:j]
            if subs not in subs_list and subs != s:
                subs_list[subs] = 0

    for item in subs_list:
        item_length = len(item)
        item_hash = sha1(item.encode("utf-8")).hexdigest()
        for i in range(len_str - item_length + 1):
            subs_hash = sha1(s[i:i + item_length].encode("utf-8")).hexdigest()
            if subs_hash == item_hash:
                subs_list[item] += 1

    return subs_list


s = input('Введите строку: ')

print(f"Количество подстрок {sum(i for i in rk(s).values())}")
