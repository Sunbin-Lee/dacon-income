## 모델 선택/ hyperparameter tuning
- **gbr + mlp 앙상블 [성능 많이 향상]**

## 중복행 존재 확인
- income 제외 중복 1680행
- **income 포함 중복 1499행 -> 한 행만 남기고 drop**
- income 제외 중복인 데이터 408개 (feature가 같은 데이터가 2개 이상)

## outlier 제거 [성능 많이 향상]
- **income status = under median / income status = over median 범주 내 outlier 제거 [now best]**

## feature engineering
- education, income_status 수정
- gain, loss, dividend binary 처리

## rmse -> outlier 영향 크게 받으므로 큰 값을 잘 맞춰야 함 & Income = 0이 많이 존재 (8697)
- stratify (income 범위 기준)
    - income 75% percentile 900
    - **income 50% percentile 530 [now best]**