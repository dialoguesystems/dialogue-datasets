# -*- coding: utf-8 -*-
import tweepy
import time
import pickle
import argparse


parser = argparse.ArgumentParser(description='distinct-n')

parser.add_argument('-data', type=str, default="twitter_ids.txt",
                    help='Path to the *-train.pt file from preprocess.py')

opt = parser.parse_args()

# these arguments can be accessed in facebook developer.
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def main():
    twitter_ids_lines = open(opt.data, "r").readlines()

    utterance_ids = []
    for twitter_ids_line in twitter_ids_lines:
        ids = [int(_id) for _id in twitter_ids_line.strip().split("	")]
        utterance_ids += ids

    id2text = {}
    utterance_cnt = len(utterance_ids)
    for index in range(0, utterance_cnt, 100):
        id_list = utterance_ids[index: index+100]
        try:
            results = api.statuses_lookup(id_list)
            for result in results:
                id2text[result.id] = result.text.encode("utf-8").replace("\n", " ")
        except:
            continue
        if index % 1000 == 0:
            print("Crawlling index = ", index)
            print("Percentage " + str(index * 1.0 / utterance_cnt) + " %")
            time.sleep(5)
        if index % 10000 == 0:
            time.sleep(120)
    pickle.dump(id2text, open("id2text.train.pkl", "w"))


if __name__ == '__main__':
    main()