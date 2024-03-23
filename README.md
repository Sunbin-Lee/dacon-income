## 현재 best : stratify_0323_engineering_3
- education, income_status 수정
- gradientboostingregressor **depth 4**
- income>875으로 stratify

- stratify_0323_engineering_1 : household, tax 수정, ohe 추가 -> 596.04
- stratify_0323_engineering_2 : household, tax 수정, ohe 추가 + working week 수정 -> 595.02
- **stratify_0323_engineering_3 : household, tax 수정, ohe 추가 + working week 수정 + capital 추가 -> 594.85**
- stratify_0323_engineering_4 : household, tax 수정, ohe 추가 + working week 수정 + capital 추가 + age -> 594.70


## rmse -> 큰 값을 잘 맞춰야 함 (1000 이상 / 2000 이상)
- stratify

## Income 분포 처리 관련

- Income == 0 : 총 8697 명
- 주로 나이 분포/직업/근무시간 등에 연관 있음 
    - **Age** < 15 -> Industry_Status == 'Not in universe or children'
    - Industry_Status == 'Not in universe or children' -> Occupation_Status == 'Unknown'
    - Industry_Status == 'Armed Forces' -> Occupation_Status == 'Armed Forces' (1개)
    - Tax_status == 'Nonfiler' -> 대부분이 'Not in universe or children'

    - Employment_Status -> 'Children or Armed Forces' 이상함
        - Armed Forces는 한 명임을 확인했는데 나이 분포는 전체적으로 퍼져 있음
    - 해당 카테고리 working/not working으로 처리 고려 / drop -> 효과 x
    
- Income = 0 / Income > 0 classification -> regression 시도 : 효과 x