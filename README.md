# 데이콘 소득 예측 AI 해커톤
- https://dacon.io/competitions/official/236230/overview/description
- 정형 | 회귀 | RMSE  

# Library
```
python 3.8.8
pandas 1.2.4
numpy 1.20.1
matplotlib 3.3.4
seaborn 0.11.1
sklearn 0.24.1
```

# Directory
```
├── data
│   ├── train.csv
│   ├── test.csv
│   └── sample_submission.csv
├── hyperparameter_search  
│   ├── data.py
│   ├── utils.py
│   └── ...
└── main.ipynb
```

# Summary
### 중복행 처리
- income 제외 중복 1680행
- **income 포함 중복 1499행 -> drop**

### outlier 제거 [성능 많이 향상]
- **income status = under median / income status = over median 범주 내 outlier 제거**

### feature engineering
- education_status, income_status 수정
- gain, loss, dividend binary 처리

### income 범위 기준 stratify 앙상블
- stratify (income 범위 기준)
    - income 75% percentile 900
    - **income 50% percentile 500**

### 모델 선택/ hyperparameter tuning [성능 많이 향상]
- **gbr + mlp 앙상블**
