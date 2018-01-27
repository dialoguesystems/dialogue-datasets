# -*- coding:utf-8 -*-
import re
from string import punctuation

def split_word_punc(text):
    words = []
    for word in text.split():
        check_mix = re.search(r'[a-z]+', word, re.I)
        if check_mix is not None and word[-1] in punctuation:
                words.append(check_mix.group())
                if word[-1] in "?!.":
                    words.append(word[-1])
        else:
            words.append(word)
    return " ".join(words)


def delete_repeat_punctuation(text):
    return re.sub(r"([%s])+" % punctuation, r"\1", text)