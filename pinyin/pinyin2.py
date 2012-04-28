#!/usr/bin/env python
# coding=utf-8

import os.path

class Pinyin():
    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), \
            'Mandarin.dat')

    def __init__(self):
        self.dict = {}
        for line in open(self.data_path):
            k, v = line.split('\t')
            self.dict[k] = v

    def get_pinyin(self, chars=u'你好'):
        result = []
        for char in chars:
            key = "%X" % ord(char)
            try:
                result.append(self.dict[key].split(" ")[0].strip()[:-1]\
                        .lower())
            except:
                result.append(char)
        return result
