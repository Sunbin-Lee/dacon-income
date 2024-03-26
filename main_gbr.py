import csv
import pandas as pd
import numpy as np
import random
import os

import argparse

import pickle

from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split, KFold, StratifiedKFold
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

from utils import *

seed_everything(42) # Seed 고정

parser = argparse.ArgumentParser()

parser.add_argument('--learning_rate', type=float, default=0.1)
parser.add_argument('--n_estimators', type=float, default=100)
parser.add_argument('--max_depth', type=float, default=3)
parser.add_argument('--min_samples_split', type=float, default=2)
parser.add_argument('--min_samples_leaf', type=float, default=1)

args = parser.parse_args()

name = f'lr_{args.learning_rate}_n_{int(args.n_estimators)}_d_{int(args.max_depth)}_s_{int(args.min_samples_split)}_leaf_{int(args.min_samples_leaf)}'

with open('data.pkl', 'rb') as f:
    trainval_x, trainval_y, test_x, income_over = pickle.load(f)

# print(np.unique(income_over))

kf = StratifiedKFold(n_splits=5, shuffle=True)

model_path = f'models/{name}'
# os.makedirs(model_path, exist_ok=True)

num_fold = 1

train_errors = [f'train_{name}']
val_errors = [f'val_{name}']
test_preds = []
for train_idx, val_idx in kf.split(trainval_x, income_over):
    train_x = trainval_x.iloc[train_idx]
    train_y = trainval_y.iloc[train_idx]
    # print(train_x.shape)

    val_x = trainval_x.iloc[val_idx]
    val_y = trainval_y.iloc[val_idx]

    fold_train_y_preds = []
    fold_val_y_preds = []

    gbr = GradientBoostingRegressor(learning_rate = args.learning_rate,
                                    n_estimators = int(args.n_estimators),
                                    max_depth = int(args.max_depth),
                                    min_samples_split = int(args.min_samples_split), # 노드 분할을 위한 최소 샘플 수
                                    min_samples_leaf = int(args.min_samples_leaf) # 리프노드 최소 샘플 수
                                    )
    gbr.fit(train_x, train_y)

    train_y_hat_gbr = gbr.predict(train_x)
    val_y_hat_gbr = gbr.predict(val_x)

    fold_train_y_preds.append(train_y_hat_gbr)
    fold_val_y_preds.append(val_y_hat_gbr)

    # pred_gbr = gbr.predict(test_x)

    # test_preds.append(pred_gbr)

    train_error = mean_squared_error(train_y, train_y_hat_gbr) ** 0.5
    val_error = mean_squared_error(val_y, val_y_hat_gbr) ** 0.5

    train_errors.append(np.round(train_error, 2))
    val_errors.append(np.round(val_error, 2))

    print(f'[{num_fold} fold] train error : {train_error:.2f} | val error : {val_error:.2f}')
    num_fold += 1

avg_train_error = sum(train_errors[1:])/5
avg_val_error = sum(val_errors[1:])/5

print(f'final train error : {avg_train_error:.2f}')
print(f'final val error : {avg_val_error:.2f}')

train_errors.append(np.round(avg_train_error, 2))
val_errors.append(np.round(avg_val_error, 2))

# final_pred = np.array(test_preds).mean(0)
# final_pred_post = np.where(final_pred<0, 0, final_pred)

# print(sum(final_pred_post>2000))

f = open('gbr.csv', 'a', newline='')
wr = csv.writer(f)
wr.writerow(train_errors)
wr.writerow(val_errors)
f.close()

# submission = pd.read_csv('data/sample_submission.csv')
# submission['Income'] = final_pred_post
# submission.to_csv(f'submission/gbr_{name}.csv', index=False)