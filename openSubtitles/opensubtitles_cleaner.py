# -*- coding:utf-8 -*-
from __future__ import division
from collections import defaultdict
import enchant
import string
import random
from utils.abbr2comp import Abbr2Comp

d = enchant.Dict("en_US")


replacer = Abbr2Comp()


def main():
    # File Reader
    src_lines = open("cleaned/train-07-11/test.src", "r").readlines()
    tgt_lines = open("cleaned/train-07-11/test.tgt", "r").readlines()

    # File Writer
    src_writer = open("2017-08-11/opensub.src", "w")
    tgt_writer = open("2017-08-11/opensub.tgt", "w")

    line_num = len(src_lines)
    assert len(src_lines) == len(tgt_lines)
    print("Starting processing ...")

    line_gram = defaultdict(int)
    src_gram = defaultdict(int)
    tgt_gram = defaultdict(int)
    for src_line, tgt_line in zip(src_lines, tgt_lines):
        src_gram[src_line] += 1
        tgt_gram[tgt_line] += 1
        line_gram[src_line + tgt_line] += 1

    print("line gram counted !")

    idx = 0
    left_pairs = 0
    for src_line, tgt_line in zip(src_lines, tgt_lines):
        if line_gram[src_line + tgt_line] < 10 and src_gram[src_line] < 10 and tgt_gram[tgt_line] < 10:
            # check word correctness
            # src_false = [token for token in src_line.split() if token[0] != "'" and not d.check(token)]
            # tgt_false = [token for token in tgt_line.split() if token[0] != "'" and not d.check(token)]

            # if len(src_false) < 1 and len(tgt_false) < 1:

            src_line = src_line.strip().lower().replace(" '", "'").replace("...", ".").split()
            tgt_line = tgt_line.strip().lower().replace(" '", "'").replace("...", ".").split()

            src_no_punc = [token for token in src_line if token not in string.punctuation]
            tgt_no_punc = [token for token in tgt_line if token not in string.punctuation]

            if len(src_no_punc) > 4 and len(tgt_no_punc) > 4 and \
                "do not" not in tgt_line and "cannot do" not in tgt_line and "don not" not in tgt_line and \
                "don t" not in tgt_line and "think so" not in tgt_line:
                src_writer.write(replacer.replace(src_line))
                tgt_writer.write(replacer.replace(tgt_line))
                left_pairs += 1
            else:
                if random.random() > 0.99:
                    src_writer.write(replacer.replace(src_line))
                    tgt_writer.write(replacer.replace(tgt_line))
                    left_pairs += 1

            if idx % 1000 == 0:
                print("[{}, {}], {:.2f}%, Left {} pairs".format(idx, line_num, idx * 100.0 / line_num, left_pairs))

        idx += 1


if __name__ == '__main__':
    main()