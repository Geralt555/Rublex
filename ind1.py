#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Дано число m(от 1 до 12 ). Определить полугодие, на которое приходится месяц
#  c номером и количество дней в том месяце (год не високосный).

if __name__ == '__main__':
    y = int(input('Введите номер месяца'))
    if y == 1:
        print('Январь ')
    elif y == 2:
        print('Февраль')
    elif y == 3:
        print('Март')
    elif y == 4:
        print('Апрель')
    elif y == 5:
        print('Май')
    elif y == 6:
        print('Июнь')
    elif y == 7:
        print('Июль')
    elif y == 8:
        print('Август')
    elif y == 9:
        print('Сентябрь')
    elif y == 10:
        print('Октябрь')
    elif y == 11:
        print('Ноябрь')
    elif y == 12:
        print('Декабрь')
    else:
        print('x <')
