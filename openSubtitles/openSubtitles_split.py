# -*- coding:utf-8 -*-
from __future__ import division
import numpy as np
import os
import argparse


parser = argparse.ArgumentParser(description='split-dataset')

parser.add_argument('-ctx_path', type=str, default="opensub_long.ctx",
                    help='Path to the context file from opensubtitles_dlg_parser.py')
parser.add_argument('-rsp_path', type=str, default="opensub_long.rsp",
                    help='Path to the response file from opensubtitles_dlg_parser.py')

parser.add_argument('-output_dir', type=str, default="/home/zeng/myGithub/openDialog-mx/data/opensub",
                    help='Path to the context file from opensubtitles_dlg_parser.py')
parser.add_argument('-train_txt_ctx', type=str, default="train.ctx",
                    help='Path to the context file from opensubtitles_dlg_parser.py')
parser.add_argument('-train_response', type=str, default="train.rsp",
                    help='Path to the response file from opensubtitles_dlg_parser.py')
parser.add_argument('-valid_txt_ctx', type=str, default="valid.ctx",
                    help='Path to the context file from opensubtitles_dlg_parser.py')
parser.add_argument('-valid_response', type=str, default="valid.rsp",
                    help='Path to the response file from opensubtitles_dlg_parser.py')
parser.add_argument('-test_txt_ctx', type=str, default="test.ctx",
                    help='Path to the context file from opensubtitles_dlg_parser.py')
parser.add_argument('-test_response', type=str, default="test.rsp",
                    help='Path to the response file from opensubtitles_dlg_parser.py')

opt = parser.parse_args()
ctx_lines = open(opt.ctx_path, "r").readlines()
rsp_lines = open(opt.rsp_path, "r").readlines()

train_context_writer = open(os.path.join(opt.output_dir, opt.train_txt_ctx), "w")
train_response_writer = open(os.path.join(opt.output_dir, opt.train_response), "w")
valid_context_writer = open(os.path.join(opt.output_dir, opt.valid_txt_ctx), "w")
valid_response_writer = open(os.path.join(opt.output_dir, opt.valid_response), "w")
test_context_writer = open(os.path.join(opt.output_dir, opt.test_txt_ctx), "w")
test_response_writer = open(os.path.join(opt.output_dir, opt.test_response), "w")

assert len(ctx_lines) == len(rsp_lines), "the length of contexts & responses are not equal!"
indexes = np.arange(len(ctx_lines))
np.random.seed(1234)
np.random.shuffle(indexes)

for i in range(2000000):
    train_context_writer.write(ctx_lines[indexes[i]])
    train_response_writer.write(rsp_lines[indexes[i]])

for i in range(2000000, 2010000):
    valid_context_writer.write(ctx_lines[indexes[i]])
    valid_response_writer.write(rsp_lines[indexes[i]])

for i in range(2010000, 2020000):
    test_context_writer.write(ctx_lines[indexes[i]])
    test_response_writer.write(rsp_lines[indexes[i]])