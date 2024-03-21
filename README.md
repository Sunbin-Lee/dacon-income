## 현재 best : feature_engineering_0319_depth_4_post
- education, income_status 수정
- gradientboostingregressor depth 4

## rmse -> 큰 값을 잘 맞춰야 함 (1000 이상 / 2000 이상)

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