#!/usr/bin/python
# -*- coding:utf-8 -*-
# 各种工具函数


def loadData(filepath):
    """加载数据"""
    print("loading data...")
    with open(filepath, "r", encoding="utf8") as f:
        raw_data = f.read()
    data = []
    raw_data = raw_data.split("\n\n")   # 将两条不同的语料分开
    for k, d in enumerate(raw_data):
        contents = []
        for token in d.split("\n"):     # 文字与实体标签
            try:
                w, e = token.split()
                contents.append((w, e))
            except:
                pass
        data.append(contents)
    print("completed!")
    return data


def word2features(sent, i):
    """返回特征列表"""
    word = sent[i][0]
    features = [
        'bias',
        'word=' + word,
    ]
    for d in (-3, -2, -1, 1, 2, 3):
        if 0 <= i + d < len(sent):
            word = sent[i+d][0]
            words = "".join([word for word, label in sent[min(i+d, i): max(i+d, i)+1]])
            features.append("%d:word=%s" % (d, word))
            features.append("%d:words=%s" % (d, words))
    return features


def sent2feature(sent):
    """返回特征"""
    return [word2features(sent, i) for i in range(len(sent))]


def sent2label(sent):
    """返回标签"""
    return [label for word, label in sent]


def sent2word(sent):
    return [word for word, label in sent]


def dataset2feature(dataset):
    print("getting features...")
    features = []
    for sent in dataset:
        features += sent2feature(sent)
    print("completed!")
    return features


def dataset2label(dataset):
    labels = []
    for sent in dataset:
        labels += sent2label(sent)
    return labels
