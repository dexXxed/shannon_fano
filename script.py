#!/usr/bin/python3
# -*- coding: utf-8 -*-
from functools import total_ordering
from math import log2


@total_ordering
class Char:
    def __init__(self, name, freq) -> None:
        self._name = name
        self._freq = freq
        self._code = ""

    def __lt__(self, other):
        return True if self._freq < other.get_freq() else False

    def __eq__(self, other):
        return True if self._name == other.get_name() and self._freq == other.get_freq() else False

    def __str__(self):
        return "{0}\t {1}\t {2}".format(self._name, str(self._freq), self._code)

    def __iter__(self):
        return self

    def get_name(self):
        return self._name

    def get_freq(self):
        return self._freq

    def get_code(self):
        return self._code

    def append_code(self, code):
        self._code += str(code)


def find_middle(lst):
    if len(lst) == 1:
        return None
    s = k = b = 0
    for p in lst:
        s += p.get_freq()
    s /= 2
    for p in range(len(lst)):
        k += lst[p].get_freq()
        if k == s:
            return p
        elif k > s:
            j = len(lst) - 1
            while b < s:
                b += lst[j].get_freq()
                j -= 1
            return p if abs(s - k) < abs(s - b) else j
    return


def shannon_fano(lst):
    middle = find_middle(lst)
    if middle is None:
        return
    for i in lst[: middle + 1]:
        i.append_code(0)
    shannon_fano(lst[: middle + 1])
    for i in lst[middle + 1:]:
        i.append_code(1)
    shannon_fano(lst[middle + 1:])


def main():
    lst = []  # создание пустого списка для сохранения вероятностей вхожжения каждого символа
    m = input("Сообщение ---> ")  # ввод самого сообщения
    s = frozenset(m)  # неизменяемое множество (кортежный словарь)
    for c in s:
        lst.append(Char(c, m.count(c)/len(m)))  # считаем вероятеости вхождения каждого символа

    lst.sort(reverse=True)  # сортирует в порядке убывания
    shannon_fano(lst)
    h = 0
    l = 0
    for c in lst:
        print(c)
        h += c.get_freq() * log2(c.get_freq())
        l += c.get_freq( ) * len(c.get_code())
    h = abs(h)
    print("H_max = {}".format(log2(len(lst))))
    print("h = {}".format(h))
    print("l_cp = {}".format(l))
    try:
        print("K_c.c. = {}".format(log2(len(lst))/l))
        print("K_o.э. = {}".format(h / l))
    except ZeroDivisionError:
        print('K_c.c. = ∞')
        print("K_o.э. = ∞")


if __name__ == "__main__":
    main()
