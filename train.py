#!/usr/bin/python
# -*- coding:utf-8 -*-

import pycrfsuite
from utils import loadData, dataset2feature, dataset2label
from config import max_iterations, model_name

# 加载训练数据集
train_data = loadData("data/example.train")
X_train = dataset2feature(train_data)
y_train = dataset2label(train_data)

# CRF模型
model = pycrfsuite.Trainer(verbose=True)
model.append(X_train, y_train)
model.set_params({
    'c1': 1.0,      # coefficient for L1 penalty
    'c2': 1e-3,    # coefficient for L2 penalty
    'max_iterations': max_iterations,  # stop earlier
    # include transitions that are possible, but not observed
    'feature.possible_transitions': True,
    # 'feature.minfreq': 3
})

# 保存模型
model.train(model_name)