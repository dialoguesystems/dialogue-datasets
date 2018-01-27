# -*- coding:utf-8 -*-
from string import punctuation
import re
# from autocorrect import spell
from utils.abbr2comp import Abbr2Comp

replacer = Abbr2Comp()


def clean_utterance(sentence):
    # 去除重复的符号而只保留一个，小写
    sentence = re.sub(r"([%s])+" % punctuation, r"\1", sentence.lower())
    # 缩写补全
    sentence = replacer.replace(sentence)
    words = []
    for word in sentence.split():
        if "@" not in word and "&" not in word and "#" not in word and "http" not in word \
                and "(" not in word and ")" not in word and len(word) < 20:
            check_mix = re.search(r'[a-z]+', word, re.I)
            if check_mix is not None:
                cleaned_word = check_mix.group()
                if len(word) > 1 and word[0].isalpha() and word[-1] in punctuation:
                    words.append(cleaned_word)
                    if word[-1] == "\"":
                        word = word[:-1]
                    if word[-1] in "?!.":
                        words.append(word[-1])
                else:
                    words.append(cleaned_word)
            else:
                words.append(word)
    return " ".join(words)


def main():
    lines = open("twitter.dlg.txt", "r").readlines()
    cleaned_writer = open("twitter.dlg.cleaned.txt", "w")
    total_lines = len(lines)
    for idx, line in enumerate(lines):
        utterances = line.strip().split("  __eou__  ")
        # First utterance.
        first_utterance = clean_utterance(utterances[0])
        # Second and after.
        other_utterances = []
        for utterance in utterances[1:]:
            other_utterances.append(clean_utterance(utterance))

        line = "  __eou__  ".join([first_utterance] + other_utterances)
        cleaned_writer.write(line + "\n")

        if idx % 2000 == 0:
            print("processing: ", idx * 1.0 / total_lines)


if __name__ == '__main__':
    main()