# -*- coding:utf-8 -*-
from __future__ import division
import random
import os
import sys
sys.path.append("../")

import time
import numpy as np
from utils.abbr2comp import Abbr2Comp
from utils.cleanSentence import cleanSentence
import utils.regexp

replacer = Abbr2Comp()
# random.seed(123)

def main():
    # File Reader
    file_path = "/home/zeng/data/opensubtitle2016/data/"
    files = os.listdir(file_path)

    # File Writer
    context_writer = open("opensub_long.ctx", "w")
    response_writer = open("opensub_long.rsp", "w")

    file_num = len(files)
    start_time = time.time()
    for idx, file in enumerate(files):
        file = os.path.join(file_path, file)
        subTitles = open(file, "r")
        context_response_pairs = []
        for subTitle in subTitles:
            subTitle = subTitle.strip().lower().replace(" '", "'")
            if len(context_response_pairs) == 0 and len(subTitle.split()) < 5:
                continue
            if len(context_response_pairs) < 6:
                # clean data in this block.
                text = cleanSentence(replacer.replace(subTitle))
                text = utils.regexp.delete_repeat_punctuation(text)
                # text = utils.regularizer.split_word_punc(text)
                context_response_pairs.append(text)
            if len(context_response_pairs) > 2 and random.random() > 0.5:
                context_average_length = np.mean([len(utterance.split()) for utterance in context_response_pairs[:-1]])
                response_length = len(context_response_pairs[-1].split())
                # print("average_length = ", context_average_length, "response_length = ", response_length)
                if context_average_length > 10 and response_length > 10:
                    # print("context_response_pairs = ", context_response_pairs)
                    context_writer.write(" __eou__ ".join(context_response_pairs[:-1]) + "\n")
                    response_writer.write(context_response_pairs[-1] + "\n")
                    context_response_pairs = []
                else:
                    context_response_pairs = context_response_pairs[1:]
            if len(context_response_pairs) == 6:
                context_response_pairs = []

        if idx % 1000 == 0:
            times = time.time() - start_time
            start_time = time.time()
            print("[{}, {}], {:.2f}%, time: {}".format(idx, file_num, idx * 100.0 / file_num, times))


if __name__ == '__main__':
    main()