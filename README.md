## 모델 선택/ hyperparameter tuning
- gradientboostingregressor **depth 4**
- mlp **activation='tanh', max_iter=500** 
- rf max_depth 조절해도 성능 안 좋았음
- **gbr + mlp 앙상블로 성능 많이 높임 [now best] [성능 많이 향상]**
- [gbr(463.77)/mlp(462.23) 예측시 output 분포 확인] - mlp가 조금 더 작게 예측하는 편

- [xgboost, lgbm 등 외부 패키지 사용 고려 및 모델 탐색]
- [gbr] min_samples_split 2 4 / min_samples_leaf 1 2 4 탐색 -> 늘려서 탐색 
- val_lr_0.05_n_500_d_4_s_16_leaf_16
- ~~[xgb] min_child_weight 1, 2, 5, 10 -> 늘려서 탐색 -> 20 이상은 의미 x~~
- ~~val_n_200_lr_0.1_d_4_child_16~~
- [mlp] hyperparameter search 필요
- scaling 고려 
- hyperparamter search GridSearchCV 이용

## 중복행 존재 확인
- income 제외 중복 1680행
- **income 포함 중복 1499행 -> 한 행만 남기고 drop**
- income 제외 중복인 데이터 408개 (feature가 같은 데이터가 2개 이상)

- feature engineering 후 중복행 처리 고려 -> 효과 x
    - 그냥 drop : 성능 감소
    - avg 고려 중 : 성능 감소

## outlier 제거 [성능 많이 향상]
- **income status = under median / income status = over median 범주 내 outlier 제거 [now best]**

## feature engineering
- education, income_status 수정
- gain, loss, dividend binary 처리

- household
- tax
- working week x

- employment status
- race ->
- marital status
- citizenship -> 

## rmse -> outlier 영향 크게 받으므로 큰 값을 잘 맞춰야 함 & Income = 0이 많이 존재 (8697)
- stratify (income 범위 기준)
    - income 75% percentile 875 (중복행 제거 시 900)
    - **income 50% percentile 500 [now best]**

## backup
- [gbr] train error : 431.07 | val error : 466.03
- [mlp] train error : 425.31 | val error : 468.87
- [mean] train error : 425.59 | val error : 464.74
--------------------------------------------------
- [gbr] train error : 433.42 | val error : 455.95
- [mlp] train error : 427.02 | val error : 454.09
- [mean] train error : 427.87 | val error : 452.53
--------------------------------------------------
- [gbr] train error : 432.88 | val error : 461.46
- [mlp] train error : 422.66 | val error : 462.26
- [mean] train error : 425.39 | val error : 459.39
--------------------------------------------------
- [gbr] train error : 430.85 | val error : 467.22
- [mlp] train error : 423.14 | val error : 467.91
- [mean] train error : 424.40 | val error : 464.76
--------------------------------------------------
- [gbr] train error : 433.96 | val error : 456.96
- [mlp] train error : 427.61 | val error : 456.98
- [mean] train error : 428.15 | val error : 454.25
--------------------------------------------------
- final train error gbr : 432.43
- final val error gbr : 461.52
- final train error xgb : 0.00
- final val error xgb : 0.00
- final train error mlp : 425.15
- final val error mlp : 462.02
- [total] final train error : 426.28
- [total] final val error : 459.13