## 모델 선택/ hyperparameter tuning
- gradientboostingregressor **depth 4**
- mlp **activation='tanh', max_iter=500** 
- rf max_depth 조절해도 성능 안 좋았음
- **gbr + mlp 앙상블로 성능 많이 높임 [now best] [성능 많이 향상]**
- [xgboost, lgbm 등 외부 패키지 사용 고려 및 모델 탐색]


## 중복행 존재 확인
- income 제외 중복 1680행
- **income 포함 중복 1499행 -> 한 행만 남기고 drop**
- drop duplicated_1_outliers_2

- income 제외 중복인 데이터 408개 (feature가 같은 데이터가 2개 이상)
- income이 다른 경우 159개 -> max/avg만 남기고 나머지 drop
- drop_duplicated_2_outliers_2 (max) | drop_duplicated_3_outliers_2 (avg)

- [feature engineering 후 중복행 처리 고려]

## outlier 제거 [성능 많이 향상]
- **income status = under median / income status = over median 범주 내 outlier 제거 [now best]**

## feature engineering
- education, income_status 수정
- household, tax, working week 수정 x | gain, loss, dividend binary 처리

- employment status
- race
- marital status
- citizenship

## rmse -> outlier 영향 크게 받으므로 큰 값을 잘 맞춰야 함
- stratify (income 범위 기준)
    - income 75% percentile 875 (중복행 제거 시 **900**)

## Income 분포 처리 ?
- Income == 0 : 총 8697 명
- 주로 나이 분포/직업/근무시간 등에 연관 있음 
    - **Age** < 15 -> Industry_Status == 'Not in universe or children'
    - Industry_Status == 'Not in universe or children' -> Occupation_Status == 'Unknown'
    - Industry_Status == 'Armed Forces' -> Occupation_Status == 'Armed Forces' (1개)
    - Tax_status == 'Nonfiler' -> 대부분이 'Not in universe or children'
    - Employment_Status -> 'Children or Armed Forces' 이상함
        - **Armed Forces는 한 명임을 확인했는데 나이 분포는 전체적으로 퍼져 있음(처리해볼 여지 있음)**
    - 해당 카테고리 working/not working으로 처리 고려 / drop -> 효과 x
- Income = 0 / Income > 0 classification -> regression 시도 : 효과 x