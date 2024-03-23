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

parser.add_argument('--hidden_layer_sizes', type=float, default=100)
parser.add_argument('--learning_rate_init', type=float, default=1e-3)
parser.add_argument('--alpha', type=float, default=1e-4)
parser.add_argument('--max_iter', type=float, default=200)

args = parser.parse_args()

name = f'hidden_{args.hidden_layer_sizes}_lr_{args.learning_rate_init}_alpha_{args.alpha}_max_iter_{args.max_iter}'

with open('data.pkl', 'rb') as f:
    trainval_x, trainval_y, test_x, income_cat = pickle.load(f)

kf = StratifiedKFold(n_splits=5, shuffle=True)

model_path = f'models/{name}'
os.makedirs(model_path, exist_ok=True)

num_fold = 1

train_errors = [name]
val_errors = [name]
for train_idx, val_idx in kf.split(trainval_x, income_cat):
    train_x = trainval_x.iloc[train_idx]
    train_y = trainval_y.iloc[train_idx]
    # print(train_x.shape)

    val_x = trainval_x.iloc[val_idx]
    val_y = trainval_y.iloc[val_idx]

    fold_train_y_preds = []
    fold_val_y_preds = []

    mlp = MLPRegressor(activation = 'tanh', 
                       hidden_layer_sizes = (int(args.hidden_layer_sizes),),
                       learning_rate_init = args.learning_rate_init,
                       alpha = args.alpha,
                       max_iter = int(args.max_iter)
                       ) 
    mlp.fit(train_x, train_y)

    # with open(f'{model_path}/mlp_{num_fold}.pkl', 'wb') as f:
    #     pickle.dump(mlp, f)

    train_y_hat_mlp = mlp.predict(train_x)
    val_y_hat_mlp = mlp.predict(val_x)

    fold_train_y_preds.append(train_y_hat_mlp)
    fold_val_y_preds.append(val_y_hat_mlp)

    pred_mlp = mlp.predict(test_x)

    train_error = mean_squared_error(train_y, train_y_hat_mlp) ** 0.5
    val_error = mean_squared_error(val_y, val_y_hat_mlp) ** 0.5

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

f = open('mlp.csv', 'a', newline='')
wr = csv.writer(f)
wr.writerow(train_errors)
wr.writerow(val_errors)
f.close()