#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Решить неравенство  , где a - произвольное действительное число.

if __name__ == '__main__':
    a = float(input())
    tmp = '= ' + str(a)
    if a >= 7 / 4:
        tmp = ' ' + str(min(a, 3 / 2 + (a - 7 / 4) ** 0.5))
    print('x <' + tmp)
