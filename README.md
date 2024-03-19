## Income == 0인 경우 해결 필요
- **Pre-processing 고려**

- 총 8697 명
- 주로 나이 분포/직업/근무시간 등에 연관 있음 
    - Industry_Status == 'Not in universe or children' 
        - Occupation_Status == 'Unknown', 'Armed Forces'와 관계 확인 필요
    - Age<15
    - Tax_status==Nonfiler, Armed Forces 확인 필요
