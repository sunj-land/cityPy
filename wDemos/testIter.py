'''
Author: sunjie
Date: 2025-03-06 23:39:26
LastEditors: sunj
LastEditTime: 2025-03-21 22:43:00
FilePath: /sunjPy/wDemos/testIter.py
'''


import reprlib
import re


RE_WORD = re.compile(r'\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


it = iter(Sentence('hell world abc'))
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break


print(__name__)
