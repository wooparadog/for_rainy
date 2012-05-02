#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
main.py
Author: WooParadog Email:  Guohaochuan@gmail.com

Created on
2012-04-24
'''
from pinyin2 import Pinyin
import doctest

parser = Pinyin()
head = {}
with open("name") as f:
    for line in f:
        name, pinyin = line.strip().decode('utf8').split()
        head[name] = pinyin

def pinyin_list_by_str(name):
    first = name[0]
    if first in head:
        result = [head[first]] + parser.get_pinyin(name[1:])
    else:
        result = parser.get_pinyin(name)

    return result


def pinyin_parser_length_2(name):
    pinyin_list = pinyin_list_by_str(name)
    return ''.join([i[:2] for i in pinyin_list])

def pinyin_parser_length_3(name):
    pinyin_list = pinyin_list_by_str(name)
    return ''.join([i[0] for i in pinyin_list[:2]]+[pinyin_list[-1][:2]])

def pinyin_parser_length_4(name):
    pinyin_list = pinyin_list_by_str(name)
    return ''.join([i[0] for i in pinyin_list])

def pinyin_parser_length_x(name):
    pinyin_list = pinyin_list_by_str(name)
    return ''.join([i[0] for i in pinyin_list[:4]])

def pinyin_parser(name):
    '''
    >>> pinyin_parser("曾蔷")
    u'zeqi'
    >>> pinyin_parser("郭浩川")
    u'ghch'
    >>> pinyin_parser("郭浩慧川")
    u'ghhc'
    >>> pinyin_parser("王浩郭慧川")
    u'whgh'
    >>> pinyin_parser("郇豪")
    u'xuha'
    '''
    name = name.decode('utf8')

    if len(name) == 2:
        result = pinyin_parser_length_2(name)
    elif len(name) == 3:
        result = pinyin_parser_length_3(name)
    elif len(name) ==4:
        result = pinyin_parser_length_4(name)
    elif len(name) > 4:
        result = pinyin_parser_length_x(name)

    return unicode(result[:4])

def main():
    doctest.testmod()

if __name__ == '__main__':
    main()
