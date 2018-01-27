# -*- coding:utf-8 -*-
import re
"""
Taken from https://github.com/inikdom/opensubtitles-parser/blob/master/opensubtitleparser.py
"""
def cleanSentence(text):
    t = text.strip('-')
    t = t.lower()
    t = t.strip('\"')
    regex = re.compile('\(.+?\)')
    t = regex.sub('', t)
    t.replace('  ', ' ')
    regex = re.compile('\{.+?\}')
    t = regex.sub('', t)
    t = t.replace('  ', ' ')
    t = t.replace("~", "")
    t = t.strip(' ')
    return t